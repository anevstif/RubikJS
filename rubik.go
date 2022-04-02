package main

import (
	"encoding/json"
	"fmt"
	"html/template"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
	//"net"
)

var PYTHON = "python3"

type TemplateData struct {
	Task     string `json:"task"`
	Solution string `json:"solution"`
	Size	 int	`json:"size"`
}

type ParseData struct {
	Task string
	Gen int
	Vis bool
	Size int 
}

//Парсинг аргументов командной строки
func parseArgs(args []string) ParseData {
	pd := ParseData{"", 0, false, 3}
	maxIndex := len(args) - 1
	if maxIndex <= 0 {
		return pd
	}
	pd.Task = args[1]
	flagCom := 0
	if (len(pd.Task)>0 && pd.Task[0] == '-') {
		pd.Task = ""
	}
	for i:= 1; i <= maxIndex; i++ {
		command := args[i]
		if flagCom > 0 {
			g, err := strconv.Atoi(command)
			if err != nil { g = 0 }
			if g < 0 { g *= -1 }
			if g > 100 { g = 100 }
			if flagCom == 1 {pd.Gen = g}
			if flagCom == 2 && g > 1 && g < 4 {pd.Size = g}
			flagCom = 0
		} else {
			if command == "-v" {
				pd.Vis = true
			}
			if command == "-g" {
				flagCom = 1
			}
			if command == "-s" {
				flagCom = 2
			}
		}
	}
	if (pd.Task == "") && (pd.Gen > 0) {
		pd.Task = generationTask(pd.Gen)
	}
	return pd
}

func checkOS() {
	if "windows" == runtime.GOOS {
		PYTHON = "python"
	}
}

func main() {
	checkOS()
    pd := parseArgs(os.Args)
	if pd.Vis == true {
		fmt.Printf("Server start with task = \"" + pd.Task + "\"\n")
		setHandleFunc(pd)
	} else {
		if pd.Task != "" {
			solution := getSolution(pd)
			fmt.Printf("%s %s",pd.Task, solution)
		}
	}
}

//Генератор задания
func generationTask(count int) string {
	face := [6]string{"U","D","F","B","L","R"}
	dir := [3]string{"","2","'"}
	task := ""
	lastSymbol := ""
	symbol := ""
	for i := 0; i < (count -1); i++ {
		for ok := true; ok; ok = (symbol == lastSymbol) {
			symbol = face[rand.Intn(6)]
		}
		task += (symbol+dir[rand.Intn(3)]+" ")
		lastSymbol = symbol
	}
	task += (face[rand.Intn(6)]+dir[rand.Intn(3)])
	return task
}

//запуск решателя на python
func fromPy(pd ParseData) string {
	n := fmt.Sprintf("%d",pd.Size)
	t := strings.Replace(pd.Task, "'", "\\'", -1)
	command := fmt.Sprintf("from solver.solver import solver%s; solver%s('%s');",n,n,t)
	cmd := exec.Command(PYTHON, "-c", command)
	out, err := cmd.Output()
	if err != nil {
		fmt.Println(err)
	}
	return (string(out))
}

// AJAX обработчики
func ajaxHandler3(w http.ResponseWriter, r *http.Request) {
	data, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	pd := ParseData{string(data),0,true,3}
	solution := getSolution(pd)
	sol := strings.Replace(solution, "\n", "", -1)
	res := &TemplateData{
		Task:     pd.Task,
		Solution: sol,
		Size: pd.Size,
	}
	a, err := json.Marshal(res)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	fmt.Printf("ajax data:\n -task: [%s]\n -solution: [%s]\n", pd.Task, sol)
	w.Write(a)
}

func ajaxHandler2(w http.ResponseWriter, r *http.Request) {
	data, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	pd := ParseData{string(data),0,true,2}
	solution := getSolution(pd)
	sol := strings.Replace(solution, "\n", "", -1)
	res := &TemplateData{
		Task:     pd.Task,
		Solution: sol,
		Size: pd.Size,
	}
	a, err := json.Marshal(res)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	fmt.Printf("ajax data:\n -task: [%s]\n -solution: [%s]\n", pd.Task, sol)
	w.Write(a)
}

func setHandleFunc(pd ParseData) {
	//создаём диспетчер путей
	mux := http.NewServeMux()
	//добавляем функцию обработчик главной страницы
	mux.HandleFunc("/", home(pd))
	mux.HandleFunc("/ajax3", ajaxHandler3)
	mux.HandleFunc("/ajax2", ajaxHandler2)
	// Инициализируем FileServer, он будет обрабатывать
	// HTTP-запросы к статическим файлам из папки "./static".
	// http.Dir путь относительно корневой папке проекта
	fileServer := http.FileServer(http.Dir("./static/"))

	// Используем функцию mux.Handle() для регистрации обработчика для
	// всех запросов, которые начинаются с "/static/". Мы убираем
	// префикс "/static" перед тем как запрос достигнет http.FileServer
	mux.Handle("/static/", http.StripPrefix("/static", fileServer))

	//запускаем сервер на порту 8081
	err := http.ListenAndServe(":8081", mux)
	if err != nil {
		fmt.Printf("error %s\n", err)
		return
	}
}

// Обработчик главной страницы.
func home(pd ParseData) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/" {
			http.NotFound(w, r)
			return
		}
		// Используем функцию template.ParseFiles() для чтения файла шаблона.
		// Если возникла ошибка, мы запишем детальное сообщение ошибки и
		// используя функцию http.Error() мы отправим пользователю
		// ответ: 500 Internal Server Error (Внутренняя ошибка на сервере)
		ts, err := template.ParseFiles("./index.html")
		if err != nil {
			log.Println(err.Error())
			http.Error(w, "Internal Server Error", 500)
			return
		}

		data := TemplateData{
			Task: pd.Task,
			Solution: getSolution(pd),
			Size: pd.Size,
		}
		// Затем мы используем метод Execute() для записи содержимого
		// шаблона в тело HTTP ответа. Последний параметр в Execute() предоставляет
		// возможность отправки динамических данных в шаблон.
		err = ts.Execute(w, data)
		if err != nil {
			log.Println(err.Error())
			http.Error(w, "Internal Server Error", 500)
		}
	}
}

func getSolution(pd ParseData) string {
	if pd.Size == 3 || pd.Size == 2 {
		return fromPy(pd)
	}
	return ""
}
