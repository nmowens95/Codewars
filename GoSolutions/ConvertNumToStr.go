// Title: Convert a Number to a String!

// Instructions:
/*
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
*/

// Answer:
package kata

import "strconv"

func NumberToString(n int) string {
	new_str := strconv.Itoa(n)
	return new_str
}

// Sample Tests:

/*
// TODO: replace with your own tests (TDD). An example to get you started is included below.
// Ginkgo BDD Testing Framework <http://onsi.github.io/ginkgo/>
// Gomega Matcher Library <http://onsi.github.io/gomega/>

package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

func dotest(n int, expected string) {
     Expect(NumberToString(n)).To(Equal(expected), "With n = %d", n)
}

var _ = Describe("Tests", func() {
     It("Sample tests", func() {
         dotest(67, "67");
         dotest(79585, "79585");
         dotest(79585, "79585");
         dotest(3, "3");
         dotest(-1, "-1");
     })
})
*/
