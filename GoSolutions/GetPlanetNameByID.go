/* Instructions


The function is not returning the correct values. Can you figure out why?

Example (Input --> Output ):

3 --> "Earth"

*/

// Answer:
package kata

func GetPlanetName(ID int) string {
    switch ID {
    case 1:
        return "Mercury"
    case 2:
        return "Venus"
    case 3:
        return "Earth"
    case 4:
        return "Mars"
    case 5:
        return "Jupiter"
    case 6:
        return "Saturn"
    case 7:
        return "Uranus"
    case 8:
        return "Neptune"
    default:
        return "Pluto" // ;-)
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

var _ = Describe("Basic Tests", func() {
    It("Should return the correct value", func() {
        Expect(GetPlanetName(2)).To(Equal("Venus"))
    })
  	It("Should return the correct value", func() {
        Expect(GetPlanetName(5)).To(Equal("Jupiter"))
    })
    It("Should return the correct value", func() {
        Expect(GetPlanetName(3)).To(Equal("Earth"))
    })
    It("Should return the correct value", func() {
        Expect(GetPlanetName(4)).To(Equal("Mars"))
    })
    It("Should return the correct value", func() {
        Expect(GetPlanetName(8)).To(Equal("Neptune"))        
    })
    It("Should return the correct value", func() {
    		Expect(GetPlanetName(1)).To(Equal("Mercury"))
    })
})
*/