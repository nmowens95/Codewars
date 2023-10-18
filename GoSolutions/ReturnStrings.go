/* Instructions
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
*/

// Answer:
package kata

func Greet(name string) string {
	return "Hello," + " " + name + " " + "how are you doing today?"
}

// Sample Tests:

/*
package kata_test

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Example test cases", func() {
  It("should return greeting for Ryan", func() {
    Expect(Greet("Ryan")).To(Equal("Hello, Ryan how are you doing today?"))
  })
})
*/
