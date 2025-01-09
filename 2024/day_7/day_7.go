package day_7

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parse_input(input []string) (int, []int) {
  key, values := input[0], input[1]
  parsed_values := []int{}

  parsed_key, _ := strconv.Atoi(key)
  for _, val := range strings.Split(values, " ") {
    parsed_val, _ := strconv.Atoi(val)
    parsed_values = append(parsed_values, parsed_val)
  }

  return parsed_key, parsed_values
}

func get_input() map[int][]int {
  file, _ := os.Open("./day_7/input.txt")
  defer file.Close()

  scanner := bufio.NewScanner(file)
  input := make(map[int][]int)
  for scanner.Scan() {
    line := scanner.Text()
    parts := strings.Split(line, ": ")
    key, values := parse_input(parts)
    input[key] = values
  }

  return input
}

func can_compute(k int, vals []int) bool {
  stack := []int {vals[0]}

  for i:=1; i<len(vals); i++ {
    next := vals[i]
    new_stack := []int{}
    for _, val := range(stack) {
      new_stack = append(new_stack, val*next, val+next)
    }
    stack = new_stack
  }

  for _, v := range(stack) {
    if v==k {
      return true
    }
  }

  return false
}

func can_compute_2(k int, vals []int) bool {
  stack := []int {vals[0]}

  for i:=1; i<len(vals); i++ {
    next := vals[i]
    new_stack := []int{}
    for _, val := range(stack) {
      concat := strings.Join([]string{strconv.Itoa(val), strconv.Itoa(next)}, "")
      concat_i, _ := strconv.Atoi(concat)
      new_stack = append(new_stack, val*next, val+next, concat_i)
    }
    stack = new_stack
  }

  for _, v := range(stack) {
    if v==k {
      return true
    }
  }

  return false
}

func process(input map[int][]int) {
  sum := 0

  for k, v := range input {
    if can_compute_2(k, v) {
      sum += k
    }
  }

  fmt.Println(fmt.Sprintf("Total calibration result: %d", sum))
}

func Run() {
  input := get_input()
  process(input)
}