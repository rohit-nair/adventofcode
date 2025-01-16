package day_15

import (
	utils "advent/utils/go"
	"advent/utils/go/collections"
	"bufio"
	"fmt"
	"os"
	"strings"
)

var ROBOT, SPACE, WALL, BOX byte = '@', '.', '#', 'O'

func find_starting_point(g collections.Grid) collections.Point {
	for m, row := range g {
		for n, c := range row {
			if c == ROBOT {
				return collections.Point{RowIdx: m, ColIdx: n}
			}
		}
	}
	panic("No starting point")
}

func score(g collections.Grid) int {
	score := 0

	for m := 0; m < len(g); m++ {
		for n := 0; n < len(g[0]); n++ {
			if g.GetAt(collections.Point{RowIdx: m, ColIdx: n}) == BOX {
				score += m*100 + n
			}
		}
	}

	return score
}

func canMove(g collections.Grid, p collections.Point) bool {
	return g.GetAt(p) == SPACE
}

func move(g collections.Grid, cur collections.Point, d collections.Direction) (collections.Grid, collections.Point) {
	m, n := cur.RowIdx, cur.ColIdx

	if m < 1 || m >= len(g)-1 ||
		n < 1 || n >= len(g[0])-1 {
		return g, cur
	}

	next_m, next_n := m+d.RowIdx, n+d.ColIdx
	next := collections.Point{RowIdx: next_m, ColIdx: next_n}
	if g.GetAt(next) == BOX {
		g, _ = move(g, next, d)
	}

	if canMove(g, next) {
		g.Swap(cur, next)
		cur = next
	}

	return g, cur
}

func getInstruction() []string {
	instructions := []string{}

	file, _ := os.Open("./day_15/input_2.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		instructions = append(instructions, strings.Split(scanner.Text(), "")...)
	}

	return instructions
}

func Run() {
	grid := utils.GetInput("./day_15/input_1.txt")
	start := find_starting_point(grid)
	instructions := getInstruction()

	moves := map[string]collections.Direction{
		"^": collections.UP,
		"v": collections.DOWN,
		"<": collections.LEFT,
		">": collections.RIGHT,
	}
	for _, m := range instructions {
		g, s := move(grid, start, moves[m])
		grid, start = g, s
	}
	fmt.Println("Score:", score(grid))
}
