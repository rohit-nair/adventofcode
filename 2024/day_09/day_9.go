package day_9

import (
	"fmt"
	"strconv"
	"strings"
)

type Info struct {
  id int
  start_idx int
  len int
  is_space bool
  mods []Info
}

func repeater(repeat int, times int) []int {
  res := []int{}
  for i:=0; i<times; i++ {
    res = append(res, repeat)
  }

  return res
}

func get_input() []int {
  res := []int {}
  k := 0
  for i, c := range strings.Split(input, "") {
    num, _ := strconv.Atoi(c)
    if i%2 == 0 {
      res = append(res, repeater(k, num)...)
      k++
    } else {
      res = append(res, repeater(-1, num)...)
    }
  }

  return res
}

func process(parsed_input []int) {
  i, j := 0, len(parsed_input)-1

  for i < j {
    for parsed_input[i] != -1 && i < len(parsed_input) {
      i++
    }

    for parsed_input[j] == -1 && j > i {
      j--
    }

    k := parsed_input[i]
    parsed_input[i] = parsed_input[j]
    parsed_input[j] = k
  }

  res := 0
  for i, v := range parsed_input {
    if v == -1 {
      continue
    }
    res += i*v
  }

  fmt.Println("Checksum is", res)
}

func get_input_2() []Info {
  res := []Info {}
  k, idx := 0, 0
  for i, c := range strings.Split(input, "") {
    num, _ := strconv.Atoi(c)
    if i%2 == 0 {
      res = append(res, Info{id:k, start_idx:idx, len:num, is_space:false})
      k++
    } else {
      res = append(res, Info{id:-1, start_idx:idx, len:num, is_space:true})
    }
    idx += num
  }

  return res
}

func find_earliest_space_to_fit(i int, input []Info) int {
  for k:=1; k<i; k += 2 {
    if input[k].id != -1 {
      panic("landed on a non-space location")
    }


    if input[k].len >= input[i].len {
      return k
    }
  }

  return -1
}

func update(i int, j int, input []Info) {
  space, file := input[j], input[i]
  
  if space.mods == nil {
    space.mods = []Info{}
  }
  space.mods = append(space.mods, Info{id:file.id, len:file.len, start_idx:space.start_idx, is_space:false})
  space.len -= file.len
  space.start_idx += file.len

  file.id = -1

  input[i] = file
  input[j] = space
}

func calc_checksum(input []Info) int {
  checksum, idx := 0, 0

  for _, i := range input {
    if i.id == -1 {
      if len(i.mods) == 0 {
        idx += i.len
        continue
      }
      for _, m := range i.mods {
        for k:=0; k<m.len; k++ {
          checksum += m.id*(idx+k)
        }
        idx += m.len
      }
      idx += i.len
      continue
    }

    for j:=0; j<i.len; j++ {
      checksum += i.id*(idx+j)
    }
    idx += i.len
  }
  
  return checksum
}

func process_2(input []Info) {
  for i:=len(input)-1; i>=0; i-=1 {
    if i%2 != 0 {
      continue
    }
    j := find_earliest_space_to_fit(i, input)
    if j == -1 {
      // no space that fits file to the left
      continue
    }
    update(i, j, input)
  }

  fmt.Println("Checksum: ", calc_checksum(input))
}

func Run() {
  // parsed_input := get_input()
  // process(parsed_input)

  parsed_input := get_input_2()
  process_2(parsed_input)
}

var input string = "2333133121414131402"