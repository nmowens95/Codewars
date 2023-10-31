// Title: Invert Values

// Instructions:
/*
Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
*/

// Answer:
package kata

func Invert(arr []int) []int {
	new_arr := []int{}
	for _, num := range arr {
		new_arr = append(new_arr, -num)
	}
	return new_arr
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

func dotest(a []int, expected []int) {
     actual := Invert(append([]int{}, a...))
     if len(expected) == 0 {
       Expect(actual).To(BeEmpty(), "With arr = %v", a)
     } else {
       Expect(actual).To(Equal(expected), "With arr = %v", a)
     }
}

var _ = Describe("Tests", func() {
     It("Sample tests", func() {
        dotest([]int{1,2,3,4,5},[]int{-1,-2,-3,-4,-5});
        dotest([]int{1,-2,3,-4,5}, []int{-1,2,-3,4,-5});
        dotest(nil, nil);
        dotest([]int{0}, []int{0})
     })
})
*/
