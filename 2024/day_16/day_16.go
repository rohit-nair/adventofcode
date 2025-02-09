package day_16

import (
	utils "advent/utils/go"
	"advent/utils/go/collections"
	"fmt"
	"math"
)

var MinScore = math.MaxInt32
var Visited = map[collections.Point]Item{}

var Moves = map[rune]collections.Direction{
	'^': collections.UP,
	'>': collections.RIGHT,
	'v': collections.DOWN,
	'<': collections.LEFT,
}

var AvailableMoves = map[collections.Direction][]collections.Direction{
	collections.UP:    {collections.LEFT, collections.RIGHT},
	collections.RIGHT: {collections.UP, collections.DOWN},
	collections.DOWN:  {collections.RIGHT, collections.LEFT},
	collections.LEFT:  {collections.DOWN, collections.UP},
}

type Item struct {
	point     collections.Point
	direction collections.Direction
	forward   int
	turns     int
}

func move(
	grid collections.Grid,
	start collections.Point,
) {

	score := func(forward int, turns int) int {
		return turns*1000 + forward
	}

	queue := []Item{{start, collections.RIGHT, 0, 0}}

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		fmt.Println("Moving to", cur.point)

		if grid.GetAt(cur.point) == '#' {
			continue
		}
		if grid.GetAt(cur.point) == 'E' {
			Visited[cur.point] = cur
			fmt.Printf("Reached end, score %d, forward %d, turn %d \n", 0, cur.forward, cur.turns)
			// if MinScore > score {
			// 	MinScore = score
			// }
			// MinVisited = visited
			continue
		}

		prev, exists := Visited[cur.point]

		if exists && score(prev.forward, prev.turns) < score(cur.forward, cur.turns) {
			// fmt.Println("Visited before ", cur)
			continue
		}

		Visited[cur.point] = cur

		next := collections.Point{RowIdx: cur.point.RowIdx + cur.direction.RowIdx, ColIdx: cur.point.ColIdx + cur.direction.ColIdx}
		// _, next_visited := Visited[next]
		// if !next_visited {
		queue = append(queue, Item{next, cur.direction, cur.forward + 1, cur.turns})
		// }

		for _, dir := range AvailableMoves[cur.direction] {
			next = collections.Point{RowIdx: cur.point.RowIdx + dir.RowIdx, ColIdx: cur.point.ColIdx + dir.ColIdx}
			// _, next_visited = Visited[next]
			// if !next_visited {
			queue = append(queue, Item{next, dir, cur.forward + 1, cur.turns + 1})
			// }
		}
	}
}

func Run() {
	grid := utils.GetInput("./day_16/example.txt")
	start, end := grid.Find('S'), grid.Find('E')

	move(grid, start)

	fmt.Println(Visited[end])
}
