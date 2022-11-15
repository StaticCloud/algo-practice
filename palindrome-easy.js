// Given an integer x, return true if x is a
// palindrome
// , and false otherwise.

// Input: x = 121
// Output: true
// Explanation: 121 reads as 121 from left to right and from right to left.

/**
 * @param {number} x
 * @return {boolean}
*/
const palindrome = (x) => {
    // by default, integers cannot be reversed, but arrays can. we can convert the integer into a string and using
    // the spread operator we can convert it to an array, from there we can reverse it and compare it to x
    let xString = x.toString();
    return xString === [...xString].reverse().join('');
}