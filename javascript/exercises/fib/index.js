// --- Directions
// Print out the n-th entry in the fibonacci series.
// The fibonacci series is an ordering of numbers where
// each number is the sum of the preceeding two.
// For example, the sequence
//  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
// forms the first ten entries of the fibonacci series.
// Example:
//   fib(4) === 3


// iterative solution
function fib(n) {
    let first = 0;
    let second = 1;
    let result = 1;

    for (i=2; i<=n; i++) {
        result = second + first;
        let temp = second;
        second += first;
        first = temp;
    }

    return result;
}

//recursive solution
// function fib(n) {
//     if (n <= 2) {
//         return 1;
//     }
//     return fib(n-1) + fib(n-2);
// }

module.exports = fib;
