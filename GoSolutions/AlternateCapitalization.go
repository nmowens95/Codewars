// Title: Alternate capitalization

// Instructions:
/*
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.
*/

// Answer:
package kata

import "strings"

func Capitalize(str string) []string {
	evenChars := ""
	oddChars := ""

	for i, char := range str {
		if i%2 == 0 {
			evenChars += strings.ToUpper(string(char))
		} else {
			evenChars += string(char)
		}
	}

	for i, char := range str {
		if i%2 == 0 {
			oddChars += string(char)
		} else {
			oddChars += strings.ToUpper(string(char))
		}
	}
	result := []string{evenChars, oddChars}
	return result
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

func dotest(st string, exp []string) {
    var ans = Capitalize(st)
    Expect(ans).To(Equal(exp))
}

var _ = Describe("Example tests", func() {
  It("It should work for basic tests", func() {
        dotest("abcdef", []string{"AbCdEf", "aBcDeF"})
        dotest("codewars", []string{"CoDeWaRs", "cOdEwArS"})
        dotest("abracadabra", []string{"AbRaCaDaBrA", "aBrAcAdAbRa"})
        dotest("codewarriors", []string{"CoDeWaRrIoRs", "cOdEwArRiOrS"})
        dotest("indexinglessons", []string{"InDeXiNgLeSsOnS", "iNdExInGlEsSoNs"})
        dotest("codingisafunactivity", []string{"CoDiNgIsAfUnAcTiViTy", "cOdInGiSaFuNaCtIvItY"})
  })
})
*/
