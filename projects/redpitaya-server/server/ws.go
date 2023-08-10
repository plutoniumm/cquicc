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

var (
	gconn    *websocket.Conn
	filepath = "./send.txt"
	sending  = false
)

func startSend() {
	for {
		data, err := ioutil.ReadFile(filepath)
		if err != nil {
			log.Println("getfile error:", err)
			return
		}

		err = gconn.WriteMessage(websocket.TextMessage, []byte(data))
		if err != nil {
			log.Println("Websocket write error:", err)
			return
		}

		time.Sleep(1 * time.Second)

		if !sending {
			return
		}
	}
}

func terminator() {
	sending = false
}

func handleWS(conn *websocket.Conn) {
	for {
		gconn = conn
		exec := Exec{}
		err := conn.ReadJSON(&exec)
		if err != nil {
			log.Println("Websocket read error:", err)
			return
		}

		fmt.Println("Received message:", exec.Run)
	}
}
