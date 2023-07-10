package main

import (
	"fmt"
	"os/exec"
	"strings"

	"github.com/valyala/fasthttp"
)

func gErr(err string, c *fasthttp.RequestCtx) []byte {
	err = "<div class='errCont'>E: " + err + "</div>"
	c.SetStatusCode(fasthttp.StatusInternalServerError)
	c.SetContentType("text/html")
	c.Write([]byte(err))
	return []byte(err)
}

func runFn(arr []string) string {
	fmt.Println("Running: " + strings.Join(arr, " "))
	cmd := exec.Command(arr[0], arr[1:]...)
	_, err := cmd.CombinedOutput()
	if err != nil {
		return err.Error()
	}
	return "200"
}

func csp(ctx *fasthttp.RequestCtx) *fasthttp.RequestCtx {
	cspValue := "default-src 'self'; script-src-elem 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:;object-src 'none';"
	ctx.Response.Header.Set("Content-Security-Policy", cspValue)
	return ctx
}
