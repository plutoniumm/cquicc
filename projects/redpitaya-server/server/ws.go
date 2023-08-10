package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"time"

	"github.com/fasthttp/websocket"
)

// {run: func, data: arbitrary}
type Exec struct {
	Run  string      `json:"run"`
	Data interface{} `json:"data"`
}

func handleWS(conn *websocket.Conn) {
	for {
		exec := Exec{}
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
