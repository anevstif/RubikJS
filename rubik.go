package main

import (
	"encoding/json"
	"fmt"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
	"strings"
	"os"
	"math/rand"
	"strconv"
)

type TemplateData struct {
	Task     string `json:"task"`
	Solution string `json:"solution"`
	Size	 int	`json:"size"`
}

//Парсинг аргументов командной строки
func parseArgs(args []string) (string, bool, int, int) {
	gen := 0
	size := 3
	vis :=false
	maxIndex := len(args) - 1
	task := args[0]
	flagCom := 0
	if (len(task)>0 && task[0] == '-') {
		task = ""
	}
	for i:= 0; i <= maxIndex; i++ {
		command := args[i]
		if flagCom > 0 {
			g, err := strconv.Atoi(command)
			if err != nil { g = 0 }
			if g < 0 { g *= -1 }
			if g > 100 { g = 100 }
			if flagCom == 1 {gen = g}
			if flagCom == 2 && g > 1 && g < 4 {size = g}
			flagCom = 0
		} else {
			if command == "-v" {
				vis = true
			}
			if command == "-g" {
				flagCom = 1
			}
			if command == "-s" {
				flagCom = 2
			}
		}
	}
	return task, vis, gen, size
}

func main() {
	task := ""
	vis := false
	gen := 0
	size := 3
	if len(os.Args) > 1 {
    	task, vis, gen, size = parseArgs(os.Args[1:])
	}
	if (task == "") && (gen > 0) {
		task = generationTask(gen)
	}
	if vis == true {
		fmt.Printf("Server start with task = \"" + task + "\"\n")
		setHandleFunc(task, size)
	} else {
		if task != "" {
			solution := getSolution(task, size)
			fmt.Printf("%s %s",task, solution)
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
func fromPy3(task string) string {
	cmd := exec.Command("python3",
		"-c",
		"from solver.solver import solver3; solver3('"+strings.Replace(task, "'", "\\'", -1)+"');")
	out, err := cmd.Output()
	if err != nil {
		fmt.Println(err)
	}
	return (string(out))
}
//запуск решателя на python
func fromPy2(task string) string {
	cmd := exec.Command("python3",
		"-c",
		"from solver.solver import solver2; solver2('"+strings.Replace(task, "'", "\\'", -1)+"');")
	out, err := cmd.Output()
	if err != nil {
		fmt.Println(err)
	}
	return (string(out))
}

// AJAX обработчикb
func ajaxHandler3(w http.ResponseWriter, r *http.Request) {
	data, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	solution := getSolution(string(data),3)
	sol := strings.Replace(solution, "\n", "", -1)
	res := &TemplateData{
		Task:     string(data),
		Solution: sol,
	}
	a, err := json.Marshal(res)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	fmt.Printf("ajax data:\n -task: [%s]\n -solution: [%s]\n", string(data), sol)
	w.Write(a)
}

func ajaxHandler2(w http.ResponseWriter, r *http.Request) {
	data, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	solution := getSolution(string(data),2)
	sol := strings.Replace(solution, "\n", "", -1)
	res := &TemplateData{
		Task:     string(data),
		Solution: sol,
	}
	a, err := json.Marshal(res)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	fmt.Printf("ajax data:\n -task: [%s]\n -solution: [%s]\n", string(data), sol)
	w.Write(a)
}

func setHandleFunc(task string, size int) {
	//создаём диспетчер путей
	mux := http.NewServeMux()
	//добавляем функцию обработчик главной страницы
	mux.HandleFunc("/", home(task, size))
	mux.HandleFunc("/ajax3", ajaxHandler3)
	mux.HandleFunc("/ajax2", ajaxHandler2)
	// Инициализируем FileServer, он будет обрабатывать
	// HTTP-запросы к статическим файлам из папки "./static".
	// Обратите внимание, что переданный в функцию http.Dir путь
	// является относительным корневой папке проекта
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
func home(task string, size int) http.HandlerFunc {
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
			Task: task,
			Solution: getSolution(task, size),
			Size: size,
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

func getSolution(task string, size int) string {
	if size == 3 {
		return fromPy3(task)
	} else if size == 2 {
		return fromPy2(task)
	}
	return ""
}
