package main

import (
	"advent/day_12"
	// "fmt"
	"runtime"
)


func main() {
  runtime.GOMAXPROCS(runtime.NumCPU())
  day_12.Run()
}