package main

import "fmt"

func funcMui(x, y int) (gg int, ss error) {

	return x + y, nil
}

type student struct {
	Name string
}
type student2 struct {
	Name string
}

func zhoujielun(v interface{}) {
	switch msg := v.(type) {
	//case *student, student:
	//	fmt.Println(msg.Name)
	case student2:
		fmt.Println(msg.Name)
	}
}
