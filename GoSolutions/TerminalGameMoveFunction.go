// Instructions:

/*
YTerminal game move function
In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.

Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

Example:
move(3, 6) should equal 15
*/

// Answer:

package kata

func Move(position int, roll int) int {
	return position + (roll * 2)
}

/*
Sample Tests:

package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Basic Tests", func() {
    It("Move(0, 4)", func() { Expect(Move(0, 4)).To(Equal(8)) })
    It("Move(3, 6)", func() { Expect(Move(3, 6)).To(Equal(15)) })
    It("Move(2, 5)", func() { Expect(Move(2, 5)).To(Equal(12)) })
})
*/
