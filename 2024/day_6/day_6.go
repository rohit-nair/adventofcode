package day_6

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strings"

	"github.com/mohae/deepcopy"
)

var DIRECTION_MAP = map[string][2]int{
	"UP":    [2]int{-1, 0},
	"DOWN":  [2]int{1, 0},
	"RIGHT": [2]int{0, 1},
	"LEFT":  [2]int{0, -1},
}

var DIRECTION_SWITCH = map[string]string{
	"UP":    "RIGHT",
	"RIGHT": "DOWN",
	"DOWN":  "LEFT",
	"LEFT":  "UP",
}

type PositionWithDirection struct {
	pos [2]int
	dir string
}

type Result struct {
	pos   map[[2]int]int
	error error
}

func read_input() ([][]string, [][]int, [2]int) {
	file, _ := os.Open("./day_6/input.txt")
	defer file.Close()

	var input [][]string
	var blocks [][]int
	var start [2]int

	scanner := bufio.NewScanner(file)
	for n := 0; scanner.Scan(); n++ {
		blocks = append(blocks, []int{})
		line := scanner.Text()
		chars := strings.Split(line, "")
		input = append(input, chars)
		for m, c := range chars {
			if c == "^" {
				start = [2]int{n, m}
			} else if c == "#" {
				blocks[n] = append(blocks[n], m)
			}
		}
	}

	return input, blocks, start
}

func update_positions(next_n int, next_m int, direction string, positions map[[2]int]int, position_n_dir map[PositionWithDirection]bool) bool {
	key_with_dir := PositionWithDirection{[2]int{next_n, next_m}, direction}
	_, exists_ := position_n_dir[key_with_dir]
	if exists_ {
		return true
	}
	position_n_dir[key_with_dir] = true

	key := [2]int{next_n, next_m}
	val, exists := positions[key]
	if exists {
		positions[key] = val + 1
	} else {
		positions[key] = 1
	}

	return false
}

func find_guard_positions(input [][]string, start [2]int, ch chan Result) Result {
	direction := "UP"
	n, m := len(input), len(input[0])
	pos_n, pos_m := start[0], start[1]

	positions := map[[2]int]int{
		{pos_n, pos_m}: 1,
	}
	position_n_dir := map[PositionWithDirection]bool{
		{pos: [2]int{pos_n, pos_m}, dir: direction}: true,
	}

	for true {
		next_n := pos_n + DIRECTION_MAP[direction][0]
		next_m := pos_m + DIRECTION_MAP[direction][1]

		if (next_n < 0 || next_n == n) || (next_m < 0 || next_m == m) {
			break
		}

		char := input[next_n][next_m]
		if char == "#" {
			direction = DIRECTION_SWITCH[direction]
		} else if char == "." || char == "^" {
			loop_detected := update_positions(next_n, next_m, direction, positions, position_n_dir)
			if loop_detected {
        res := Result{nil, errors.New("Loop detected")}
        if ch != nil {
          ch <- res 
        }
				return res
			}
			pos_n, pos_m = next_n, next_m
		} else {
			panic(fmt.Sprintf("Unknown character %s", char))
		}
	}
  
  if ch != nil {
    ch <- Result{positions, nil}
  }
	return Result{positions, nil}
}

func Run() {
	input, _, start := read_input()

	res := find_guard_positions(input, start, nil)
	pos_map, _ := res.pos, res.error
  distinct_positions := len(pos_map)
	fmt.Println(distinct_positions)

	loops := 0
	ch := make(chan Result, distinct_positions-1)
	for pos, _ := range pos_map {
		if pos == start {
			continue
		}

		input_ := deepcopy.Copy(input).([][]string)
		input_[pos[0]][pos[1]] = "#"
		go find_guard_positions(input_, start, ch)
	}

  for i:=0; i < len(pos_map)-1; i++ {
    res := <-ch
    if res.error != nil {
      loops += 1
    }
  }

	fmt.Println(fmt.Sprintf("Loops detected %d", loops))
}

var puzzle_input string = `
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
`
