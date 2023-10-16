// Instructions

/*
Finish the solution so that it sorts the passed in array of numbers.
If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution(c(1, 2, 3, 10, 5)) # should return c(1, 2, 3, 5, 10)
solution(NULL)              # should return NULL

*/

// Answer:
package kata

import (
	"sort"
)

func SortNumbers(numbers []int) []int {
	if numbers == nil || len(numbers) == 0 {
		return []int{}
	}
	sort.Ints(numbers)
	return numbers
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Sample Test Cases", func() {
  It("should work for sample tests", func() {
    Expect(Expect(SortNumbers([]int{1, 2, 10, 50, 5})).To(Equal([]int{1,2,5,10,50})))
    Expect(Expect(SortNumbers([]int{})).To(Equal([]int{})))
*/
