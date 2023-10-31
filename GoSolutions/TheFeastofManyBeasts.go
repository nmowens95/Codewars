// Title: The Feast of Many Beasts

// Instructions:
/*
All of the animals are having a feast! Each animal is bringing one dish.
There is just one rule: the dish must start and end with the same letters as the animal's name.
For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.

Write a function feast that takes the animal's name and dish as arguments
and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.

Assume that beast and dish are always lowercase strings, and that each has at least two letters.
beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.
*/

// Answer:
package kata

func Feast(beast string, dish string) bool {
	if dish[0] == beast[0] && dish[len(dish)-1] == beast[len(beast)-1] {
		return true
	}
	return false
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
  It("should return the correct value", func() {
    Expect(Feast("great blue heron", "garlic naan")).To(BeTrue(), "Testing 'great blue heron' vs 'garlic naan'")
    Expect(Feast("chickadee", "chocolate cake")).To(BeTrue(), "Testing 'chickadee' vs 'chocolate cake'")
    Expect(Feast("brown bear", "bear claw")).To(BeFalse(), "Testing 'brown bear' vs 'bear claw'")
  })
})
*/
