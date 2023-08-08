package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"time"

	"github.com/fasthttp/router"
	"github.com/fasthttp/websocket"
	"github.com/valyala/fasthttp"
)

var (
	upgrader = websocket.FastHTTPUpgrader{
		ReadBufferSize:  1024,
		WriteBufferSize: 1024,
	}
	filepath = "./data.json"
)

type Executer struct {
	Run  string      `json:"run"`
	Data interface{} `json:"data"`
}

func handleWS(conn *websocket.Conn) {
	for {
		var exec Executer
		err := conn.ReadJSON(&exec)
		if err != nil {
			log.Println("Websocket read error:", err)
			return
		}

		fmt.Println("Received message:", exec.Run)

		switch string(exec.Run) {
		case "start":
			log.Println("Start sending data.json")
			for {
				data, err := ioutil.ReadFile(filepath)
				if err != nil {
					log.Println("getJSON error:", err)
					return
				}

				err = conn.WriteMessage(websocket.TextMessage, []byte(data))
				if err != nil {
					log.Println("Websocket write error:", err)
					return
				}

				time.Sleep(1 * time.Second)
			}
		case "stop":
			log.Println("Stop sending data.json")
			return
		default:
			fmt.Println(exec)
		}
	}
}

func main() {
	r := router.New()

	var PORT string
	if len(os.Args) > 1 {
		PORT = os.Args[1]
	} else {
		PORT = "1337"
	}

	r.ServeFiles("/assets/{filepath:*}", "./assets")

	// index.html
	r.GET("/", func(ctx *fasthttp.RequestCtx) {
		data, err := ioutil.ReadFile("./index.html")
		if err != nil {
			log.Fatal(err)
		}

		ctx.SetContentType("text/html")
		ctx.Write(data)
	})

	r.GET("/ws", func(ctx *fasthttp.RequestCtx) {
		err := upgrader.Upgrade(ctx, func(conn *websocket.Conn) {
			handleWS(conn)
		})
		if err != nil {
			log.Println("Websocket upgrade error:", err)
			return
		}

		defer ctx.Response.ConnectionClose()
	})

	log.Println("Server listening on port " + PORT)
	log.Fatal(fasthttp.ListenAndServe(":"+PORT, r.Handler))
}
