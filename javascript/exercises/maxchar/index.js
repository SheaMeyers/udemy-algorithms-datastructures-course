// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function getCharMap(str) {
    const chars = {};
    for (let char of str) {
        chars[char] = chars[char] + 1 || 1;
    }
    return chars;
}

function maxChar(str) {
    const charMap = getCharMap(str);
    let maxChar;
    let maxValue = 0;
    for (char in charMap) {
        if (charMap[char] > maxValue) {
            maxValue = charMap[char];
            maxChar = char;
        }
    }
    return maxChar;
}

module.exports = maxChar;
