/* Instructions
An AI has infected a text with a character!!

This text is now fully mutated to this character.

If the text or the character are empty, return an empty string.
There will never be a case when both are empty as nothing is going on!!

Note: The character is a string of length 1 or an empty string.

Example
text before = "abc"
character   = "z"
text after  = "zzz"
*/

// Answer:
package kata

func Contamination(text, char string) string {
	new_text := ""
	if text == "" || char == "" {
		return ""
	} else {
		for range text {
			new_text += char
		}
	}
	return new_text
}

// Sample Tests:

/*
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

func dotest(text, char, expected string) {
     Expect(Contamination(text, char)).To(Equal(expected), "With text = \"%s\", char = \"%s\"", text, char)
}

var _ = Describe("Tests", func() {
     It("Sample tests", func() {
        dotest("abc","z", "zzz")
        dotest("","z", "")
        dotest("abc","", "")
        dotest("_3ebzgh4","&", "&&&&&&&&")
        dotest("//case"," ", "      ")
     })
})
*/
