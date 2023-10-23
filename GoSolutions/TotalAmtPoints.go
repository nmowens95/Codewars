// Title: Total Amount of Points

// Instructions:
/*
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
*/

// Answer:
package kata

func Points(games []string) int {
	x := 0
	for _, game := range games {
		if game[0] > game[2] {
			x += 3
		} else if game[0] == game[2] {
			x++
		}
	}
	return x
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Basic Tests", func() {
   It("Testing for Points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])", func() {
     Expect(Points([]string{"1:0","2:0","3:0","4:0","2:1","3:1","4:1","3:2","4:2","4:3"})).To(Equal(30))
   })
   It("Testing for points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'])", func() {
     Expect(Points([]string{"1:1","2:2","3:3","4:4","2:2","3:3","4:4","3:3","4:4","4:4"})).To(Equal(10))
   })
   It("Testing for points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4'])", func() {
     Expect(Points([]string{"0:1","0:2","0:3","0:4","1:2","1:3","1:4","2:3","2:4","3:4"})).To(Equal(0))
   })
   It("Testing for points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'])", func() {
     Expect(Points([]string{"1:0","2:0","3:0","4:0","2:1","1:3","1:4","2:3","2:4","3:4"})).To(Equal(15))
   })
   It("Testing for points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'])", func() {
     Expect(Points([]string{"1:0","2:0","3:0","4:4","2:2","3:3","1:4","2:3","2:4","3:4"})).To(Equal(12))
   })
})
*/
