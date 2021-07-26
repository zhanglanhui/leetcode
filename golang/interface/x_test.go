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

type Student2 struct{}

func (stu *Student2) Speak(think string) (talk string) {
	if think == "love" {
		talk = "You are a good boy"
	} else {
		talk = "hi1"
	}
	return
}

func Test1(t *testing.T) {
	var peo People = &Student{}
	var peo2 People = &Student2{}
	think := "love1"
	fmt.Println(peo.Speak(think))
	fmt.Println(peo2.Speak(think))
}
