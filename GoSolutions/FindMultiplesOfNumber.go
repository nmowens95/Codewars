// Title: Find Multiples of a Number

// Instructions:
/*
In this simple exercise, you will build a program that takes a value, integer ,
and returns a list of its multiples up to another value, limit . If limit is a multiple of integer,
it should be included as well. There will only ever be positive integers passed into the function,
not consisting of 0. The limit will always be higher than the base.

For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6
are the multiples of 2 up to 6.
*/

// Answer:
package kata

func FindMultiples(integer, limit int) []int {
	new_list := []int{}
	for i := integer; i <= limit; i += integer {
		new_list = append(new_list, i)
	}
	return new_list
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Tests", func() {
  It("Basic Tests", func() {
    Expect(FindMultiples(5, 25)).To(Equal([]int{5, 10, 15, 20, 25}))
    Expect(FindMultiples(1, 2)).To(Equal([]int{1, 2}))
  })
})
*/
