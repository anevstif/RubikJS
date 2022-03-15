package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"
    "io/ioutil"
)

type TemplateData struct {
	Task     string
	Solution string
}

func main() {
	var task string
	if len(os.Args) > 1 {
		task = os.Args[1]
	} else {
		task = ""
	}
	fmt.Printf("Server start with task = \"" + task + "\"\n")
	setHandleFunc(task)
}

// AJAX Request Handler
func ajaxHandler(w http.ResponseWriter, r *http.Request) {
    //*
	data, err := ioutil.ReadAll(r.Body);
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
	fmt.Printf("ajax data: [% s]\n", string(data))
    w.Write(data)
    w.Write([]byte("consectetur adipisicing elit."))
}



func setHandleFunc(task string) {
	//создаём диспетчер путей
	mux := http.NewServeMux()
	//добавляем функцию обработчик главной страницы
	mux.HandleFunc("/", home(task))

	mux.HandleFunc("/ajax", ajaxHandler)

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
		return
	}
}

// Обработчик главной страницы.
func home(task string) http.HandlerFunc {
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

		// Затем мы используем метод Execute() для записи содержимого
		// шаблона в тело HTTP ответа. Последний параметр в Execute() предоставляет
		// возможность отправки динамических данных в шаблон.

		data := TemplateData{
			Task:     task,
			Solution: getSolution(task),
		}

		err = ts.Execute(w, data)
		if err != nil {
			log.Println(err.Error())
			http.Error(w, "Internal Server Error", 500)
		}
	}
}

func getSolution(task string) string {
	return "L2 D'"
}
