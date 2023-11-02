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

func QuarterOf(month int) int {
	if month <= 3 {
		return 1
	} else if month <= 6 {
		return 2
	} else if month <= 9 {
		return 3
	} else {
		return 4
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

var _ = Describe("Test Example", func() {
  It("should test example values", func() {
    Expect(QuarterOf(3)).To(Equal(1))
    Expect(QuarterOf(8)).To(Equal(3))
    Expect(QuarterOf(11)).To(Equal(4))
  })
})
*/
