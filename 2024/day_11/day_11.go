package day_11

import (
	"fmt"
	"strconv"
	// "strings"
)

// func process(input []string) []string {
	// new_input := []string {}
	// for _, c := range input {
	// 	num, _ := strconv.Atoi(c)
	// 	// 1. 0 -> 1
	// 	if num == 0 {
	// 		new_input = append(new_input, "1")
	// 	} else if len(c) % 2 == 0 {
	// 	// 2. split even
	// 		new_input = append(new_input, c[:len(c)/2])
	// 		trailing, _ := strconv.Atoi(c[len(c)/2:])
	// 		new_input = append(new_input, strconv.Itoa(trailing))
	// 	} else {
	// 	// 3. mul 2024
	// 		new_input = append(new_input, strconv.Itoa(num*2024))
	// 	}
	// }
	// return new_input
// }

func process(input map[int]int) map[int]int {
	new_input := make(map[int]int)
	for stone, count := range input {
		c := strconv.Itoa(stone)
		// 1. 0 -> 1
		if stone == 0 {
		  new_input[1] += count
		} else if len(c) % 2 == 0 {
		// 2. split even
			leading, _ := strconv.Atoi(c[len(c)/2:])
			trailing, _ := strconv.Atoi(c[:len(c)/2])
			new_input[leading] += count
			new_input[trailing] += count
		} else {
		// 3. mul 2024
			new_input[stone*2024] += count
		}
	}
	return new_input
}

func Run() {
	input := map[int]int {125:1, 17:1}
	for i:=0; i<25; i++ {
		input = process(input)
	}

	stones := 0
	for _, v := range input {
		stones += v
	}
	fmt.Println("Number of stones: ", stones)
}