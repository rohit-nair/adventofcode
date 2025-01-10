package main

import (
	"advent/day_11"
	// "fmt"
	"runtime"
)


func main() {
  runtime.GOMAXPROCS(runtime.NumCPU())
  day_11.Run()
}