package day_10

import (
	"bufio"
  "fmt"
	"os"
	"strconv"
	"strings"

	"github.com/mohae/deepcopy"
)

func get_input() ([][]int, [][]int) {
  file, _ := os.Open("./day_10/input.txt")
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

func move(input [][]int, prev_val int, cur []int, summit string, trailheads_summits_map map[string]map[string]int, visited map[string]bool) {
  m, n := len(input), len(input[0])

  if cur[0] < 0 || cur[0] >= m || cur[1] < 0 || cur[1] >= n {
    return
  }

  key := fmt.Sprintf("%d-%d", cur[0], cur[1])
  val := input[cur[0]][cur[1]]

  _, has_visited := visited[key]
  if has_visited {
    return
  }

  if prev_val - val != 1 {
    return
  }

  visited[key] = true
  
  if val == 0 {
    // found trailhead, add to map
    _, trailhead_visited := trailheads_summits_map[key]
    if trailhead_visited == false {
      trailheads_summits_map[key] = make(map[string]int)
    }

    trailheads_summits_map[key][summit] += 1
    return
  }

  for _, m := range MOVES {
    move(input, val, []int{m[0]+cur[0], m[1]+cur[1]}, summit, trailheads_summits_map, deepcopy.Copy(visited).(map[string]bool))
  }
}

var UP, DOWN, LEFT, RIGHT = []int{-1, 0}, []int{1, 0}, []int{0, -1}, []int{0, 1}
var MOVES = [][]int{UP, DOWN, LEFT, RIGHT}

func Run() {
  input, summits := get_input()

  trailheads_summits_map := make(map[string]map[string]int)
  for _, s := range summits {
    key := fmt.Sprintf("%d-%d", s[0], s[1])
    visited := make(map[string]bool)
    move(input, 10, s, key, trailheads_summits_map, visited)
  }

  score := 0
  for _, v := range trailheads_summits_map {
    for _, p := range v {
      score += p
    }
  }
  fmt.Println("Score:",score)
}