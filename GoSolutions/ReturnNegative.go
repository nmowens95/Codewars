// Instructions

/*
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Examples
MakeNegative(1)    // return -1
MakeNegative(-5)   // return -5
MakeNegative(0)    // return 0
Notes
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
*/

// Answer:
package kata

func MakeNegative(x int) int {
	if x == 0 {
		return x
	} else if x > 0 {
		return -x
	}
	return x
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Test Example", func() {
  It("should test that the solution returns the correct value", func() {
    Expect(MakeNegative(42)).To(Equal(-42))
  })
})
*/
