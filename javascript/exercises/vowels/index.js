// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

function vowels(str) {
    const vowelsConstants = ['a','e','i','o','u','A','E','I','O','U'];
    let numVowels = 0;
    for (let char of str) {
        if(vowelsConstants.includes(char)) {
            numVowels += 1;
        }
    }
    return numVowels;
}

module.exports = vowels;
