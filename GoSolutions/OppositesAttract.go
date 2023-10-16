/* Instructions
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
*/

// Answer:
package kata

func LoveFunc(flower1, flower2 int) bool {
	if flower1%2 != flower2%2 {
		return true
	} else {
		return false
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
var _ = Describe("Tests", func() {
  It("Basic Tests", func() {
    Expect(LoveFunc(1,4)).To(Equal(true))
    Expect(LoveFunc(2,2)).To(Equal(false))
    Expect(LoveFunc(0,1)).To(Equal(true))
    Expect(LoveFunc(0,0)).To(Equal(false))
  })
})
*/
