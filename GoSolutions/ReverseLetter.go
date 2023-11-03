// Title: Simple Fun #176: Reverse Letter

// Instructions:
/*
Task
Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.

[output] a string

*/

// Answer:
package kata

import "unicode"

func reverse(str string) (result string) {
	for _, v := range str {
		result = string(v) + result
	}
	return
}

func ReverseLetters(str string) string {
	newString := ""
	for _, s := range str {
		if unicode.IsLetter(s) {
			newString += string(s)
		}
	}
	return reverse(newString)
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

func dotest(s, expected string) {
     Expect(ReverseLetters(s)).To(Equal(expected), "With s = \"%s\"", s)
}

var _ = Describe("Tests", func() {
     It("Sample tests", func() {
        dotest("krishan","nahsirk")
        dotest("ultr53o?n","nortlu")
        dotest("ab23c","cba")
        dotest("krish21an","nahsirk")
        dotest("", "")
     })
})
*/
