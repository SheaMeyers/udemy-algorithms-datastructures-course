// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// with N levels using the # character.  Make sure the
// pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'

function lengthOfCharacters(n) {
    return n + (n-1)
}

function pyramid(n) {
    const totalLength = lengthOfCharacters(n);
    for (let i=1; i<=n; i++) {
        let hashtagCharactersToShow = lengthOfCharacters(i);
        let spacesToShow = (totalLength - hashtagCharactersToShow)/2;
        let stringToPrint = '';
        for (let j=0; j<spacesToShow; j++) {
            stringToPrint += ' ';
        }
        for (let j=0; j<hashtagCharactersToShow; j++) {
            stringToPrint += '#';
        }
        for (let j=0; j<spacesToShow; j++) {
            stringToPrint += ' ';
        }
        console.log(stringToPrint);
    }
}

module.exports = pyramid;
