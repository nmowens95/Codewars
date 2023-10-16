// Instructions:

/*
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
*/

// Answer:

package kata

import (
	"strings"
)

func StringToArray(str string) []string {
	words := strings.Split(str, " ")
	return words
}

/*
Sample Tests:

package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Tests", func() {
     It("Sample tests", func() {
       Expect(StringToArray("Robin Singh")).To(Equal([]string{"Robin", "Singh"}))
       Expect(StringToArray("CodeWars")).To(Equal([]string{"CodeWars"}))
       Expect(StringToArray("I love arrays they are my favorite")).To(Equal([]string{"I", "love", "arrays", "they", "are", "my", "favorite"}))
       Expect(StringToArray("1 2 3")).To(Equal([]string{"1", "2", "3"}))
     })
})
*/
