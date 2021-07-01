package main

import "fmt"

// 1.
func main4() {
	s := make([]int, 0, 5)
	fmt.Println(cap(s))
	s = append(s, 1, 2, 3, 4, 5, 6)
	fmt.Println(cap(s))
}

//// 2.
//func main() {
//	s := make([]int, 0)
//	s = append(s, 1, 2, 3, 4)
//	fmt.Println(s)
//}
