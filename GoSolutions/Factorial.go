// Title: Quarter of the year

// Instructions:
/*
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12
*/

// Answer:
package kata

func Factorial(n int) int {
	if n <= 1 {
		return 1
	} else {
		return n * Factorial(n-1)
	}
}

// Sample Tests:

/*
package kata_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	. "codewarrior/kata"
)

var _ = Describe("Example Tests",func() {
	It("basic tests", func() {
		tests_arr := [...][2]int{
			{0,1},
			{1,1},
			{4,24},
			{7,5040},
			{17,355687428096000},
		}
		for _,v := range tests_arr {Expect(Factorial(v[0])).To(Equal(v[1]))}
	})
})
*/
