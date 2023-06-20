package main

import "fmt"

func IsPalindrome1(input string) bool {
    for i := 0; i < len(input); i++ {
        if input[i] != input[len(input) - 1 - i] {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(IsPalindrome1("abcba"))
    fmt.Println(IsPalindrome1("abc"))
}
