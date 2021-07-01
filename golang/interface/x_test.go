package channel

import (
	"fmt"
	"testing"
)

type People interface {
	Speak(string) string
}

type Student struct{}

func (stu *Student) Speak(think string) (talk string) {
	if think == "love" {
		talk = "You are a good boy"
	} else {
		talk = "hi"
	}
	return
}

func Test1(t *testing.T) {
	var peo People = &Student{}
	think := "love1"
	fmt.Println(peo.Speak(think))
}
