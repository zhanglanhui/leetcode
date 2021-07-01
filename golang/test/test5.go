package main

import "fmt"

type People struct {
	Name string
}

func (p *People) String() string {
	return fmt.Sprintf("print: %v", p)
}

func main5() {
	p := &People{}
	fmt.Println(p.String())
}
