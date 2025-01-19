package day_15_2

import (
	utils "advent/utils/go"
	"advent/utils/go/collections"
	"bufio"
	"fmt"
	"os"
	"strings"
)

var ROBOT, SPACE, WALL, BOX, BOX_START, BOX_END byte = '@', '.', '#', 'O', '[', ']'

func score(g collections.Grid) int {
	score := 0

	for m := 0; m < len(g); m++ {
		for n := 0; n < len(g[0]); n++ {
			if g.GetAt(collections.Point{RowIdx: m, ColIdx: n}) == BOX_START {
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
		n < 2 || n >= len(g[0])-2 {
		return g, cur
	}

	next_m, next_n := m+d.RowIdx, n+d.ColIdx
	next := collections.Point{RowIdx: next_m, ColIdx: next_n}
	if g.GetAt(next) == BOX_START || g.GetAt(next) == BOX_END {
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

	file, _ := os.Open("./day_15/example_2.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		instructions = append(instructions, strings.Split(scanner.Text(), "")...)
	}

	return instructions
}

func double_grid(g collections.Grid) collections.Grid {
	res := collections.Grid{}

	for m, row := range g {
		res = append(res, []byte{})
		for _, c := range row {
			switch c {
			case WALL:
				res[m] = append(res[m], WALL, WALL)
			case SPACE:
				res[m] = append(res[m], SPACE, SPACE)
			case ROBOT:
				res[m] = append(res[m], ROBOT, SPACE)
			case BOX:
				res[m] = append(res[m], BOX_START, BOX_END)
			}
		}
	}
	return res
}

func Run() {
	grid := utils.GetInput("./day_15/example_1.txt")
	grid = double_grid(grid)
	start := grid.Find(ROBOT)
	instructions := getInstruction()

	grid.Print()
	fmt.Println(start, instructions)

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
