package day_3

import (
	"fmt"
	"regexp"
	"strconv"
)

func Run() {
	re_mul := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	matches_mul := re_mul.FindAllStringIndex(input, -1)

	re_do := regexp.MustCompile(`do\(\)`)
	matches_do := re_do.FindAllStringIndex(input, -1)

	re_dont := regexp.MustCompile(`don't\(\)`)
	matches_dont := re_dont.FindAllStringIndex(input, -1)

	res := 0
	i := min(matches_mul[0][0], matches_do[0][0], matches_dont[0][0])
	for i < len(input) && len(matches_mul) > 0 {
		if i == matches_mul[0][0] {
			res += calc_mul(matches_mul[0][0], matches_mul[0][1])
			i = matches_mul[0][1]
			_, matches_mul = pop(matches_mul)
		} else if len(matches_do) > 0 && i == matches_do[0][0] {
			i = matches_do[0][1]
			_, matches_do = pop(matches_do)
		} else if len(matches_dont) > 0 && i == matches_dont[0][0] {
			if len(matches_do) > 0 {
				i = matches_do[0][1]
				_, matches_do = pop(matches_do)

				for len(matches_mul) > 0 && i > matches_mul[0][0] {
					_, matches_mul = pop(matches_mul)
				}

				for len(matches_dont) > 0 && i > matches_dont[0][0] {
					_, matches_dont = pop(matches_dont)
				}
			} else {
				// No more dos
				break
			}
		} else {
			i++
		}
	}

	fmt.Println(res)
}

func pop(slice [][]int) ([]int, [][]int) {
	return slice[0], slice[1:]
}

func calc_mul(start, end int) int {
	s := input[start+4 : end]
	nums := regexp.MustCompile(`(\d+),(\d+)`).FindAllStringSubmatch(s, -1)
	res := 1
	for _, num := range nums {
		a, _ := strconv.Atoi(num[1])
		b, _ := strconv.Atoi(num[2])
		res *= a * b
	}
	return res
}

func part_1() {
	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	matches := re.FindAllStringSubmatch(input, -1)

	res := 0
	for i := 0; i < len(matches); i++ {
		m, _ := strconv.Atoi(matches[i][1])
		n, _ := strconv.Atoi(matches[i][2])

		res += m * n
	}

	fmt.Println(res)
}

var input_ string = `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`

var input string = ``
