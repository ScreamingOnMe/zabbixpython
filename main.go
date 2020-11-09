package main

import (
	"fmt"
	"reflect"
)

func printhellowolrd(msg string) {
	typemsg := reflect.TypeOf(msg)
	k := typemsg.Kind()
	if k != reflect.String {
		fmt.Println("you are wrong!")
	} else {
		fmt.Println(msg + "helloworld!")
	}
}

func main() {
	printhellowolrd("lijian print ")
}
