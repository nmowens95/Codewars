// Title: altERnaTIng cAsE <=> ALTerNAtiNG CaSe

// Instructions:
/*
Define String.prototype.toAlternatingCase (or a similar
function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase
in your selected language; see the initial solution for details) such that each
lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

ToAlternatingCase("hello world"); // => "HELLO WORLD"
ToAlternatingCase("HELLO WORLD"); // => "hello world"
ToAlternatingCase("hello WORLD"); // => "HELLO world"
ToAlternatingCase("HeLLo WoRLD"); // => "hEllO wOrld"
ToAlternativeCase("12345"); // => "12345" (Non-alphabetical characters are unaffected)
ToAlternativeCase("1a2b3c4d5e"); // => "1A2B3C4D5E"
ToAlternativeCase("String.prototype.toAlternatingCase"); // => "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
*/

// Answer:
package kata

import "unicode"

func ToAlternatingCase(str string) string {
	newStr := ""
	for _, s := range str {
		if unicode.IsUpper(s) {
			newStr += string(unicode.ToLower(s))
		} else if unicode.IsLower(s) {
			newStr += string(unicode.ToUpper(s))
		} else {
			newStr += string(s)
		}
	}
	return newStr
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
  It("basic tests", func() {
    Expect(ToAlternatingCase("hello world")).To(Equal("HELLO WORLD"))
    Expect(ToAlternatingCase("HELLO WORLD")).To(Equal("hello world"))
    Expect(ToAlternatingCase("hello WORLD")).To(Equal("HELLO world"))
    Expect(ToAlternatingCase("HeLLo WoRLD")).To(Equal("hEllO wOrld"))
    Expect(ToAlternatingCase("12345")).To(Equal("12345"))
    Expect(ToAlternatingCase("1a2b3c4d5e")).To(Equal("1A2B3C4D5E"))
    Expect(ToAlternatingCase("String.prototype.toAlternatingCase")).To(Equal("sTRING.PROTOTYPE.TOaLTERNATINGcASE"))
    Expect(ToAlternatingCase(ToAlternatingCase("Hello World"))).To(Equal("Hello World"))
    Expect(ToAlternatingCase("altERnaTIng cAsE")).To(Equal("ALTerNAtiNG CaSe"))
    Expect(ToAlternatingCase("ALTerNAtiNG CaSe")).To(Equal("altERnaTIng cAsE"))
    Expect(ToAlternatingCase("altERnaTIng cAsE <=> ALTerNAtiNG CaSe")).To(Equal("ALTerNAtiNG CaSe <=> altERnaTIng cAsE"))
    Expect(ToAlternatingCase("ALTerNAtiNG CaSe <=> altERnaTIng cAsE")).To(Equal("altERnaTIng cAsE <=> ALTerNAtiNG CaSe"))
  })
})
*/
