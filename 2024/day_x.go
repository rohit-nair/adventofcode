package main

import (
	"advent/day_14"
	// "fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	day_14.Run()
}
