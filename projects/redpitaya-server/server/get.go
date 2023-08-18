package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/valyala/fasthttp"
)

func dataHandler(ctx *fasthttp.RequestCtx) {
	ctx.SetContentType("text/plain")
	ctx.SetStatusCode(fasthttp.StatusOK)

	// if no file is specified, return list of files
	if ctx.UserValue("file") == nil {
		files, err := ioutil.ReadDir("./data")
		if err != nil {
			log.Fatal(err)
		}

		list := ""
		for _, f := range files {
			list += f.Name() + "\n"
		}

		csp(ctx).Write([]byte(list))
		return
	}

	// otherwise, return the file
	file := ctx.UserValue("file").(string)

	data, err := ioutil.ReadFile("./data/" + file)
	if err != nil {
		ctx.SetStatusCode(fasthttp.StatusNotFound)
		csp(ctx).Write([]byte("No Such File"))
	}

	csp(ctx).Write(data)
}

func killSwitch(ctx *fasthttp.RequestCtx) {
	ctx.SetContentType("text/plain")
	ctx.SetStatusCode(fasthttp.StatusOK)

	killType := ctx.UserValue("type").(string)
	fmt.Println("Got kill request for: " + killType)
	switch killType {
	case "parent":
		cmd := runFn([]string{"sh", "./main.sh", "stop"})
		if cmd != "200" {
			fmt.Println("Couldn't kill proc: " + cmd)
		}
		os.Exit(0)
		return

	case "child":
		cmd := runFn([]string{"sh", "./main.sh", "stop"})
		if cmd != "200" {
			gErr("Couldn't kill proc: "+cmd, ctx)
			return
		}
		csp(ctx).Write([]byte("He was taken from us too soon."))
	}
	return
}
