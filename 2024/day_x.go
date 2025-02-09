package main

import (
	"advent/day_16"
	// "fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	day_16.Run()
}
