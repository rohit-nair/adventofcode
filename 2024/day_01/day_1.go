package day_1

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func Run() {
	file, err := os.Open("day_1/input.txt")
	if err != nil {
		fmt.Println("error opening file:", err)
		return
	}
	defer file.Close()

	var arr_1 []int
	var arr_2 []int

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		nums := strings.Split(line, "   ")
		// fmt.Println(nums)

		num_1, _ := strconv.Atoi(nums[0])
		num_2, _ := strconv.Atoi(nums[1])

		arr_1 = append(arr_1, num_1)
		arr_2 = append(arr_2, num_2)
	}

	sort.Ints(arr_1)
	sort.Ints(arr_2)

	find_diff(arr_1, arr_2)
	find_similarity_score(arr_1, arr_2)
}

func find_diff(arr_1 []int, arr_2 []int) {
	diff := 0

	for i := 0; i < len(arr_1); i++ {
		diff += int(math.Abs(float64(arr_1[i] - arr_2[i])))
	}

	fmt.Println(diff)
}

func find_frequency(arr_1 []int) map[int]int {
	frequency := make(map[int]int)
	for _, num := range arr_1 {
		frequency[num]++
	}
	return frequency
}

func find_similarity_score(arr_1 []int, arr_2 []int) {
	arr_1_freq := find_frequency(arr_1)
	arr_2_freq := find_frequency(arr_2)

	similarity_score := 0
	for k, v := range arr_1_freq {
		similarity_score += v * k * arr_2_freq[k]
	}

	fmt.Printf("Similarity score: %d", similarity_score)
}
