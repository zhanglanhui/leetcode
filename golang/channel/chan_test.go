package channel

import (
	"fmt"
	_ "net/http/pprof"
	"testing"
)

func TestChanel(t *testing.T) {
	// 创建一个整型通道
	ch := make(chan int)
	// 尝试将0通过通道发送
	ch <- 0
}

var complete chan int = make(chan int)

func loop() {
	for i := 0; i < 10; i++ {
		fmt.Printf("%d ", i)
	}

	complete <- 0 // 执行完毕了，发个消息
}

func TestChanel2(t *testing.T) {
	go loop()
	<-complete // 直到线程跑完, 取到消息. main在此阻塞住
}
