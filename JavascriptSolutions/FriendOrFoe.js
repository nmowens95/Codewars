/*
Instructions:

Make a program that filters a list of strings and returns a 
list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it 
has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
*/

// Answer:

function friend(friends){
    let friend_list = []
    
    for (i = 0; i < friends.length; i++){
      if (friends[i].length === 4 && isNaN(friends[i])) {
        friend_list.push(friends[i])
      }
    }
    return friend_list
  }

/*
Sample Tests:
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {
    assert.deepEqual(friend(["Ryan", "Kieran", "Mark"]), ["Ryan", "Mark"])
    assert.deepEqual(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
    assert.deepEqual(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])
    assert.deepEqual(friend(["Love", "Your", "Face", "1"]), ["Love", "Your", "Face"])
  })
})
*/