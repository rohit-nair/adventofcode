package day_10

import (
	"bufio"
	"fmt"
	// "fmt"
	"os"
	"strconv"
	"strings"
)

func get_input() ([][]int, [][]int) {
  file, _ := os.Open("./day_10/example.txt")
  defer file.Close()

  scanner := bufio.NewScanner(file)
  input := [][]int{}
  summits := [][]int{}
  m := 0
  for scanner.Scan() {
    line := scanner.Text()
    input = append(input, []int{})
    for n, c := range strings.Split(line, "") {
      c_int, _ := strconv.Atoi(c)
      input[m] = append(input[m], c_int)
      if c_int == 9 {
        summits = append(summits, []int{m, n})
      }
    }
    m++
  }

  return input, summits
}

func process([][]int) {
  
}

func Run() {
  _, summits := get_input()

  trailheads := make(map[string]int)
  // process(input)
}