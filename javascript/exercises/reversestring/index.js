// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
    const stringLength = str.length;
    let reversedString = '';

    for(let i=1; i<=stringLength; i++) {
        reversedString = reversedString + str[stringLength-i];
    }

    // for (let character of str) {
    //     reversedString = character + reversedString;
    // }

    return reversedString;
}

// function reverse(str) {
//     return str.split('').reduce((rev, char) => char + rev, '');
// }

// function reverse(str) {
//     // return str.split('').reverse().join('');
//     const array = str.split('');
//     array.reverse()
//     return array.join('');
// }


module.exports = reverse;
