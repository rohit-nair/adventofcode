package utils

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"advent/utils/go/collections"
)

func GetInput(path string) collections.Grid {
	file, error := os.Open(path)
	defer file.Close()

	if error != nil {
		fmt.Println("Error encountered while attempting to read file")
	}

	grid := collections.Grid{}
	scanner := bufio.NewScanner(file)

	for m := 0; scanner.Scan(); m++ {
		grid = append(grid, []byte{})
		for _, c := range strings.Split(scanner.Text(), "") {
			grid[m] = append(grid[m], c[0])
		}
	}
	fmt.Println(fmt.Sprintf("Returning grid of size %dx%d", len(grid), len(grid[0])))

	return grid
}
