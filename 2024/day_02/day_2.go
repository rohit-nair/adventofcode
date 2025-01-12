package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)


func main() {
  file, _ := os.Open("input.txt") 
  defer file.Close()

  scanner := bufio.NewScanner(file)

  safe_reports := 0
  for scanner.Scan() {
    line := scanner.Text()
    fields := strings.Split(line, " ")
    fmt.Println(fields)

    safe := satisfies_criteria(fields)
    if safe {
      safe_reports++
    } else if try_dampener(fields) {
      safe_reports++
    }
  }

  fmt.Printf("Safe reports: %d", safe_reports)
}

func satisfies_criteria(fields []string) bool {
  var prev *int
  var asc *bool
  safe := true

  for _, lvl := range fields {
    num, _ := strconv.Atoi(lvl)
    if prev == nil {
      prev = &num
      continue
    }

    delta := math.Abs(float64(num - *prev))
    if delta < 1 || delta > 3 {
      fmt.Println("Breaking as out of levels")
      safe = false
      break
    }

    if asc == nil {
      is_greater := num > *prev
      asc = &is_greater
      prev = &num
      continue
    }

    diff := num - *prev
    if (diff > 0 && !*asc) || (diff < 0 && *asc) {
      fmt.Println("Breaking as not monotonic")
      safe = false
      break
    }
    *prev = num
  }

  return safe
}

func try_dampener(fields []string) bool {
  for i := 0; i < len(fields); i++ {
    copy_fields := append([]string {}, fields...)
    mod_fields := append(copy_fields[:i], copy_fields[i+1:]...)

    if satisfies_criteria(mod_fields) {
      return true
    }
  }
  return false
}

func part_1() {
  file, _ := os.Open("day_2.txt") 
  defer file.Close()

  scanner := bufio.NewScanner(file)

  safe_reports := 0
  for scanner.Scan() {
    line := scanner.Text()
    fields := strings.Split(line, " ")
    
    var prev *int
    var asc *bool
    safe := true
      
    for _, lvl := range fields {
      num, _ := strconv.Atoi(lvl)
      if prev == nil {
        prev = &num
        continue
      }

      delta := math.Abs(float64(num - *prev))
      // fmt.Printf("delta %d \n", int(delta))
      if delta < 1 || delta > 3 {
        fmt.Println("Breaking as out of levels")
        safe = false
        break
      }
      
      if asc == nil {
        is_greater := num > *prev
        asc = &is_greater
        prev = &num
        continue
      }

      diff := num - *prev
      if (diff > 0 && !*asc) || (diff < 0 && *asc) {
        fmt.Println("Breaking as not monotonic")
        safe = false
        break
      }
      *prev = num
    }
    if safe {
      safe_reports++
    }
  }

  fmt.Printf("Safe reports: %d", safe_reports)
}