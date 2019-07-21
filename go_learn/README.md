https://milapneupane.com.np/2019/07/06/learning-golang-from-zero-to-hero/

### base
1. package main
说明这个是可执行文件而不是共享库，是一个入口。
2. GOPATH, GOROOT


### Variables
var a int // will be zero
var a = 1 // automatically assigned as an int
message := "hello world" // a shorthand definition for the variable declaraion
var b,c int = 2, 3

### Data types 
- int, int8, int16, int64, uint, uint32 and so on
- string
- bool // var a bool = true

- array // var a [5]int
        // var multiD [2][3]int
        // b := [2]string{"a", "b"}
        // the compiler count for you
        // b := [...]string{"a", "b"} 

        // can't change, can't get subarray
        // An array variable denotes the entire array, not a pointer
        // assign or pass around an array you make a copy of its content
        // you can use a pointer

- slice // var b []int // zero capacity and zero length
        // numbers := make([]int, 5) length 5, capacity 5
        // numbers := make([]int, 5, 10) length 5, capacity 10
        // letters := []string{"a", "b", "c"}

        // b := []byte{'g', 'o', 'l', 'a', 'n', 'g'}
        // b[1:4] == []byte{'o', 'l', 'a'}
        // x := b[:]

        
        // slice internals
