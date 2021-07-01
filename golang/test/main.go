package main

import "fmt"

func main1() {
	var s = []int{1, 2, 3}
	s1 := append(s, []int{4, 5, 6}...)
	fmt.Println(s1)
}
