package day_4

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func Run() {
  res := 0

  matrix := get_input()

  rows := len(matrix)
  cols := len(matrix[0])

  for m:=0; m<rows; m++ {
    for n:=0; n<cols; n++ {
      if matrix[m][n] == "M" ||  matrix[m][n] == "S" {
        res += count_x_mas(matrix, m, n)
      }
    }
  }

  fmt.Println(res)
}

func count_x_mas(matrix [][]string, m int, n int) int {
  rows := len(matrix)
  cols := len(matrix[0])

  if m <= rows-1-2 {
    if n <= cols-1-2 {
      // top->right
      elems := []string{
        matrix[m][n],
        matrix[m+1][n+1],
        matrix[m+2][n+2],
      }
      text := strings.Join(elems, "")
      if !(text == "MAS" || text == "SAM") {
        return 0
      }

      // top->left
      elems = []string{
        matrix[m][n+2],
        matrix[m+1][n+1],
        matrix[m+2][n],
      }
      text = strings.Join(elems, "")
      if text == "MAS" || text == "SAM" {
        return 1
      }
    }
  }

  return 0
}

func part_1() {
  res := 0
  
  matrix := get_input()
  res += count_xmas(matrix)

  t_matrix := transpose(matrix)
  res += count_xmas(t_matrix)

  res += calc_diagonal_xmas(matrix)
  
  fmt.Println(res)
}

func get_input() [][]string {
  file, _ := os.Open("./day_4/input.txt") 
  defer file.Close()

  scanner := bufio.NewScanner(file)

  var matrix [][]string
  for scanner.Scan() {
    l := scanner.Text()
    if len(l) > 0 {
      matrix = append(matrix, strings.Split(l, ""))
    }
  }

  return matrix
}

func count_xmas(matrix [][]string) int {
  re_xmas := regexp.MustCompile("XMAS")
  re_samx := regexp.MustCompile("SAMX")

  res := 0
  for _, l := range(matrix) {
    line := strings.Join(l, "")
    res += len(re_xmas.FindAllStringSubmatchIndex(line, -1))
    res += len(re_samx.FindAllStringSubmatchIndex(line, -1))
  }
  return res
}

func calc_diagonal_xmas(matrix [][]string) int {
  res := 0
  rows := len(matrix)
  cols := len(matrix[0])

  for m:=0; m<rows; m++ {
    for n:=0; n<cols; n++ {
      if matrix[m][n] == "X" ||  matrix[m][n] == "S" {
        res += xmas_in_diagonal(matrix, m, n)
      }
    }
  }

  return res
}

func xmas_in_diagonal(matrix [][]string, m int, n int) int {
  res := 0
  rows := len(matrix)
  cols := len(matrix[0])

  if m <= rows-1-3 {
    // top->right
    if n <= cols-1-3 {
      elems := []string{
        matrix[m][n],
        matrix[m+1][n+1],
        matrix[m+2][n+2],
        matrix[m+3][n+3],
      }
      text := strings.Join(elems, "")
      if text == "XMAS" || text == "SAMX" {
        res++
      }
    }

    // top->left
    if n >= 3 {
      elems := []string{
        matrix[m][n],
        matrix[m+1][n-1],
        matrix[m+2][n-2],
        matrix[m+3][n-3],
      }
      text := strings.Join(elems, "")
      if text == "XMAS" || text == "SAMX" {
        res++
      }
    }
  }

  return res
}

func transpose(matrix [][]string) [][]string {
  rows := len(matrix)
  cols := len(matrix[0])

  t_matrix := make([][]string, cols)
  for i, _ := range t_matrix {
    t_matrix[i] = make([]string, rows)
  }

  for i := 0; i < rows; i++ {
      for j := 0; j < cols; j++ {
          t_matrix[j][i] = matrix[i][j]
      }
  }
  return t_matrix
}