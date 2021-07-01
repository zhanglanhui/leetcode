package channel

import (
	"fmt"
	"testing"
)

func TestChanel3(t *testing.T) {
	ch := make(chan int, 1000)
	go func() {
		for i := 0; i < 10; i++ {
			ch <- i
		}
	}()
	go func() {
		for {
			a, ok := <-ch
			if !ok {
				fmt.Println("close")
				return
			}
			fmt.Println("a: ", a)
		}
	}()
	defer close(ch)
	fmt.Println("ok")
	//time.Sleep(time.Second * 1)
}
