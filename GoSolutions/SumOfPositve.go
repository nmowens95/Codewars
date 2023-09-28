// Instructions:

/*
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.

*/

// Answer:

package kata

func PositiveSum(numbers []int) int {
	total := 0
	for _, nums := range numbers {
		if nums == 0 {
			return 0
		}
		if nums > 0 {
			total += nums
		}
	}
	return total
}

/*
Sample Tests:
package kata_test

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Fixed Tests", func() {
  It("should test that the solution returns the correct value", func() {
    Expect(PositiveSum([]int{1, 2, 3, 4, 5})).To(Equal(15))
    Expect(PositiveSum([]int{1, -2, 3, 4, 5})).To(Equal(13))
    Expect(PositiveSum([]int{})).To(Equal(0))
    Expect(PositiveSum([]int{-1, -2, -3, -4, -5})).To(Equal(0))
    Expect(PositiveSum([]int{-1, 2, 3, 4, -5})).To(Equal(9))
  })
})
*/
