package main

import (
	"advent/day_13"
	// "fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	day_13.Run()
}
