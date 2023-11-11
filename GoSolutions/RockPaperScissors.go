/* Instructions
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
*/

// Answer:
package kata

func Rps(p1, p2 string) string {
	if p1 == "rock" && p2 == "scissors" || p1 == "scissors" && p2 == "paper" || p1 == "paper" && p2 == "rock" {
		return "Player 1 won!"
	} else if p1 == p2 {
		return "Draw!"
	}
	return "Player 2 won!"
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
     It("Sample tests", func() {
       Expect(Rps("rock","scissors")).To(Equal("Player 1 won!"))
       Expect(Rps("scissors","rock")).To(Equal("Player 2 won!"))
       Expect(Rps("rock","rock")).To(Equal("Draw!"))
     })
})
*/
