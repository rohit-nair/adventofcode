package day_5

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Run() {
  rules := get_rules()
  input := get_input()

  fmt.Println(calc_score_part_2(input, rules))
}

func calc_score_part_2(input []string, rules map[string]bool) int {
  res := 0

  for _, l := range input {
    pages := strings.Split(l, ",")

    if valid, _, _ := is_valid(pages, rules); valid {
      continue
    }
    
    for true {
      if valid, i, j := is_valid(pages, rules); !valid {
        k := pages[i]
        pages[i] = pages[j]
        pages[j] = k
      } else {
        break
      }
    }

    mid := pages[len(pages)/2]
    page, _ := strconv.Atoi(mid)
    res += page
  }

  return res
}

func calc_score(input []string, rules map[string]bool) int {
  res := 0

  for _, l := range input {
    pages := strings.Split(l, ",")
    if valid, _, _ := is_valid(pages, rules); valid {
      mid := pages[len(pages)/2]
      page, _ := strconv.Atoi(mid)
      res += page
    }
  }

  return res
}

func is_valid(pages []string, rules map[string]bool) (bool,int,int) {
  for i:=0; i<len(pages)-1; i++ {
    for j:=i+1; j<len(pages); j++ {
      comb := []string{pages[j],pages[i]}
      _, exists := rules[strings.Join(comb, "|")]
      if exists {
        return false, i, j
      }
    }
  }
  return true, -1, -1
}

func get_rules() map[string]bool {
  file, _ := os.Open("./day_5/rules.txt") 
  defer file.Close()

  scanner := bufio.NewScanner(file)

  rules := make(map[string]bool)
  for scanner.Scan() {
    l := scanner.Text()
    rules[l] = true
  }

  return rules
}

func get_input() []string {
  file, _ := os.Open("./day_5/input.txt") 
  defer file.Close()

  scanner := bufio.NewScanner(file)

  input := []string{}
  for scanner.Scan() {
    l := scanner.Text()
    input = append(input, l)
  }

  return input
}