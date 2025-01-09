package day_8

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Pos struct {
  m int
  n int
}

func read_input() ([]int, map[string][][]int) {
  file, _ := os.Open("./day_8/input.txt")
  defer file.Close()

  scanner := bufio.NewScanner(file)
  m, col := 0, 0
  nodes := make(map[string][][]int)
  for scanner.Scan() {
    line := scanner.Text()

    for n, c := range strings.Split(line, "") {
      col = max(col, n)
      
      if c == "." {
        continue
      }

      pos, exists := nodes[c]
      if exists == false {
        nodes[c] = [][]int{{m, n}} 
      } else {
        nodes[c] = append(pos, []int {m, n})
      }
    }
    m++
  }

  return []int{m, col+1}, nodes
}

func count_antinodes(size []int, cur []int, next []int, antinodes map[Pos]int) {
  pos_1 := Pos{cur[0] - (next[0]-cur[0]), cur[1] - (next[1]-cur[1])}
  if pos_1.m >= 0 && pos_1.m < size[0] {
    if pos_1.n >= 0 && pos_1.n < size[1] {
      antinodes[pos_1]++
    }
  }


  pos_2 := Pos{next[0] + (next[0]-cur[0]), next[1] + (next[1]-cur[1])}
  if pos_2.m >= 0 && pos_2.m < size[0] {
    if pos_2.n >= 0 && pos_2.n < size[1] {
      antinodes[pos_2]++
    }
  }
}

func process(size []int, input map[string][][]int) {
  antinodes := make(map[Pos]int)
  for _, v := range input {
    for i:=0; i<len(v)-1; i++ {
      cur := v[i]
      for j:=i+1; j<len(v); j++ {
        count_antinodes(size, cur, v[j], antinodes)
      }
    } 
  }

  // fmt.Println(antinodes)
  fmt.Println(fmt.Sprintf("Antinodes: %d", len(antinodes)))
}

func Run() {
  size, input := read_input()
  process(size, input)
}