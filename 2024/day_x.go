package main

import (
	day_15_2 "advent/day_15"
	// "fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	day_15_2.Run()
}
