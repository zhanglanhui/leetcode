package turn

import (
	"fmt"
	"sync"
	"testing"
)

func TestLetter(t *testing.T) {
	i := 'A'
	i++
	fmt.Println(string(i))
}

func TestTurn(t *testing.T) {
	letter, number := make(chan bool), make(chan bool)
	wait := sync.WaitGroup{}

	go func() {
		i := 1
		for {
			select {
			case <-number:
				fmt.Print(i)
				i++
				fmt.Print(i)
				i++
				letter <- true
			}
		}
	}()
	wait.Add(1)
	go func(wait *sync.WaitGroup) {
		i := 'A'
		for {
			select {
			case <-letter:
				if i >= 'Z' {
					wait.Done()
					return
				}

				fmt.Print(string(i))
				i++
				fmt.Print(string(i))
				i++
				number <- true
			}
		}
	}(&wait)
	number <- true
	wait.Wait()
}
