package main

import (
	"advent/day_10"
	// "fmt"
	"runtime"
)


func main() {
  runtime.GOMAXPROCS(runtime.NumCPU())
  day_10.Run()
}