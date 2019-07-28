https://milapneupane.com.np/2019/07/06/learning-golang-from-zero-to-hero/
https://blog.golang.org/go-slices-usage-and-internals

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

        // 有点类似指针的概念
        // b[1:4] == []byte{'o', 'l', 'a'}

        // x := b[:]

        // slice internals
        the distinction between length and capacity
        A slice cannot be grown beyond its capacity.

        // double the slices
        t := make([]byte, len(s), (cap(s) +1)*2)
        copy(t, s)
        s = t

        // append
        append(s, 1,2,3,4)
        t := []byte{5,6,7}
        s = append(s, t...)
        
        // slice doesn't make a copy of the underlying array
        // a simple way
        c := make([]int, 5)
        copy(c, b)
        return c


### packages
    // install
    go get github.com/satori/go.uuid

    go install 
    use either method
    - mv package into go/src 
    - set go path

	package person


	func Description(name string) string {
		return "the Person name is: " + name
	}

	func secretName(name string) string {
		// """ this is private """
		return "Do not share"
	}   

    // 启动一个go的文档
    godoc -http=":8080"



In Go, panic is not the ideal way to handle exceptions in a program. It is recommended to use an error object instead. When a panic occurs, the program execution get’s halted. The thing that gets executed after a panic is the defer.
