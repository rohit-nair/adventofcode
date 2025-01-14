package day_14

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

type Grid struct{ rows, cols int }
type Position struct{ x, y, vx, vy int }

var robot_map = map[int]Position{}

func (g *Grid) step(p Position) Position {
	m_, n_ := (p.x+p.vx)%g.cols, (p.y+p.vy)%g.rows
	if m_ < 0 {
		m_ += g.cols
	}
	if n_ < 0 {
		n_ += g.rows
	}
	return Position{m_, n_, p.vx, p.vy}
}

func (g *Grid) robots_in_quadrant() int {
	quadrants := [4]int{0, 0, 0, 0}

	x_mid, y_mid := int(g.cols/2), int(g.rows/2)

	for _, v := range robot_map {
		if v.x < x_mid && v.y < y_mid {
			quadrants[0]++
		} else if v.x > x_mid && v.y < y_mid {
			quadrants[1]++
		} else if v.x > x_mid && v.y > y_mid {
			quadrants[3]++
		} else if v.x < x_mid && v.y > y_mid {
			quadrants[2]++
		}
	}

	res := 1
	for _, r := range quadrants {
		res *= r
	}
	return res
}

func (g *Grid) Score() (int, int) {

	x_mid, y_mid := int(g.cols/2), int(g.rows/2)

	dx, dy := 0, 0
	for _, v := range robot_map {
		dx += v.x - x_mid
		dy += v.y - y_mid
	}

	return dx, dy
}

func (g *Grid) Print() {
	robots := map[string]int{}
	for _, v := range robot_map {
		robots[fmt.Sprintf("%d-%d", v.x, v.y)]++
	}

	for i := 0; i < g.rows; i++ {
		for j := 0; j < g.cols; j++ {
			_, exists := robots[fmt.Sprintf("%d-%d", j, i)]
			if exists {
				fmt.Print("*")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Print("\n")
	}
}

func get_input() {
	file, _ := os.Open("./day_14/input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		var x, y, vx, vy int
		fmt.Sscanf(scanner.Text(), "p=%d,%d v=%d,%d", &x, &y, &vx, &vy)
		robot_map[i] = Position{x, y, vx, vy}
	}
}

func Run() {
	m, n := 103, 101
	min_score, min_iteration := math.MaxInt32, 0
	grid := Grid{m, n}

	get_input()

	for i := 0; i < m*n*2; i++ {
		for r := 0; r < len(robot_map); r++ {
			robot_map[r] = grid.step(robot_map[r])
		}

		score := grid.robots_in_quadrant()
		if score < min_score {
			min_score = score
			min_iteration = i
		}
		if i == 6242 {
			grid.Print()
		}
	}

	fmt.Println(min_score, min_iteration)
}
