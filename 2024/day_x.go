package main

import (
	"advent/day_15"
	// "fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	day_15.Run()
}
