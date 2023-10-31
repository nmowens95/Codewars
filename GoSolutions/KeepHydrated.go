// Title: Keep Hydrated!

// Instructions:
/*
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink,
rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
*/

// Answer:
package kata

func Litres(time float64) int {
	return int(time * 0.5)
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Test Examples", func() {
	It("Should return the correct values for the sample test cases!", func() {
		Expect(Litres(2)).To(Equal(1))
    Expect(Litres(1.4)).To(Equal(0))
    Expect(Litres(12.3)).To(Equal(6))
    Expect(Litres(0.82)).To(Equal(0))
    Expect(Litres(11.8)).To(Equal(5))
    Expect(Litres(1787)).To(Equal(893))
    Expect(Litres(0)).To(Equal(0))
  })
})
*/
