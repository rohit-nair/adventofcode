package collections

import "fmt"

type Point struct{ RowIdx, ColIdx int }
type Direction Point

var UP, DOWN, LEFT, RIGHT = Direction{-1, 0}, Direction{1, 0}, Direction{0, -1}, Direction{0, 1}

var MOVES = map[string]Direction{
	"UP":    UP,
	"DOWN":  DOWN,
	"LEFT":  LEFT,
	"RIGHT": RIGHT,
}

type Grid [][]byte

// Find character in the grid
// f: character to find
func (g Grid) Find(f byte) Point {
	for m, row := range g {
		for n, c := range row {
			if c == f {
				return Point{RowIdx: m, ColIdx: n}
			}
		}
	}
	panic("No starting point")
}

func (g Grid) Len() int {
	return len(g)
}

func (g Grid) Get(index int) []byte {
	return g[index]
}

func (g Grid) GetAt(p Point) byte {
	return g[p.RowIdx][p.ColIdx]
}

func (g *Grid) Swap(a, b Point) {
	k := (*g)[a.RowIdx][a.ColIdx]
	(*g)[a.RowIdx][a.ColIdx] = (*g)[b.RowIdx][b.ColIdx]
	(*g)[b.RowIdx][b.ColIdx] = k
}

func (g Grid) Print() {
	for _, row := range g {
		for _, c := range row {
			fmt.Print(string(c))
		}
		fmt.Println("")
	}
}
