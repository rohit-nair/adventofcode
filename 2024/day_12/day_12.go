package day_12

import (
	"fmt"
	"math"

	"gonum.org/v1/gonum/mat"
)

type Pos struct {
	x int
	y int
}

func solve(input []Pos, ch chan int) int {
	// solutions := []Pos{}
	A, B, P := input[0], input[1], input[2]
	// cost := int(math.Pow(2, 32))
	cost := math.MaxInt32

	for a := 0; a < 1000000000; a++ {
		for b := 0; b < 10000000; b++ {
			if A.x*a+B.x*b == P.x+10000000000000 &&
				A.y*a+B.y*b == P.y+10000000000000 {
				fmt.Println(a, b)
				cost = min(cost, a*3+b)
			}
		}
	}

	if ch != nil {
		ch <- cost
	}
	return cost
}

func isInteger(value float64) bool {
	return math.Abs(value-math.Round(value)) < 1e-9
}

func solve_2(input []Pos, ch chan int) int {
	A, B, P := input[0], input[1], input[2]

	// Define matrix A
	mat_A := mat.NewDense(2, 2, []float64{
		float64(A.x), float64(B.x),
		float64(A.y), float64(B.y),
	})

	// Define vector b
	// b := mat.NewVecDense(2, []float64{float64(P.x), float64(P.y)})
	b := mat.NewVecDense(2, []float64{float64(P.x + 10000000000000), float64(P.y + 10000000000000)})

	// Solve for x
	var x mat.VecDense
	err := x.SolveVec(mat_A, b)
	if err != nil {
		fmt.Println("Error:", err)
		return 0
	}

	cost := 0
	if isInteger(x.AtVec(0)) && isInteger(x.AtVec(1)) {
		cost = int(x.AtVec(0))*3 + int(x.AtVec(1))
	}

	ch <- cost
	return cost
}

func Run() {
	// input := [][]Pos {
	// 	{Pos{94, 34}, Pos{22, 67}, Pos{8400, 5400}},
	// 	{Pos{26, 66}, Pos{67, 21}, Pos{12748, 12176}},
	// 	{Pos{17, 86}, Pos{84, 37}, Pos{7870, 6450}},
	// 	{Pos{69, 23}, Pos{27, 71}, Pos{18641, 10279}},
	// }
	input := get_input()

	ch := make(chan int, len(input))
	total := 0
	for _, i := range input {
		go solve_2(i, ch)
	}
	for i := 0; i < len(input); i++ {
		cost := <-ch
		total += cost
	}
	fmt.Println(total)
}

func get_input() [][]Pos {
	var foo = []Pos{
		Pos{94, 34}, Pos{22, 67}, Pos{8400, 5400},
		Pos{26, 66}, Pos{67, 21}, Pos{12748, 12176},
		Pos{17, 86}, Pos{84, 37}, Pos{7870, 6450},
		Pos{69, 23}, Pos{27, 71}, Pos{18641, 10279},
	}
	input := [][]Pos{}

	for i := 0; i < len(foo); i += 3 {
		input = append(input, []Pos{foo[i+0], foo[i+1], foo[i+2]})
	}
	return input
}
