// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

// For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

//     I can be placed before V (5) and X (10) to make 4 and 9. 
//     X can be placed before L (50) and C (100) to make 40 and 90. 
//     C can be placed before D (500) and M (1000) to make 400 and 900.

// Given a roman numeral, convert it to an integer.

// not difficult, but there is a lot of repetition
// create a sum variable and respectfully append the correct value to it depending on the symbol
// easy for single symbol roman numerals, but a little trickier for I, X, and C, since the following numeral
// can effect the value

const romanToInt = (s) => {
    let sum = 0;

    // we can check if s still has a value and run the operation while it does
    while (s) {
        // check the first value at index 0 and then chop down the array from the front
        if (s.indexOf('I') === 0) {
            // i is a special case, since the following value can effect how much we append to sum
            // we can check (in this case) if index 0 is IX, and then append the appropriate number
            // instead of shortening the string by 1 character, we do it by 2
            if (s.indexOf('IX') === 0) {
                sum = sum + 9;
                s = s.substring(2)
            } else if (s.indexOf('IV') === 0) {
                sum = sum + 4;
                s = s.substring(2)
            } else {
                sum = sum + 1;
                s = s.substring(1)
            }
        } else if (s.indexOf('V') === 0) {
            sum = sum + 5;
            s = s.substring(1)
        } else if (s.indexOf('X') === 0) {
            if (s.indexOf('XC') === 0) {
                sum = sum + 90;
                s = s.substring(2)
            } else if (s.indexOf('XL') === 0) {
                sum = sum + 40;
                s = s.substring(2)
            } else {
                sum = sum + 10;
                s = s.substring(1)
            }
        } else if (s.indexOf('L') === 0) {
            sum = sum + 50;
            s = s.substring(1)
        } else if (s.indexOf('C') === 0) {
            if (s.indexOf('CM') === 0) {
                sum = sum + 900;
                s = s.substring(2)
            } else if (s.indexOf('CD') === 0) {
                sum = sum + 400;
                s = s.substring(2)
            } else {
                sum = sum + 100;
                s = s.substring(1)
            }
        } else if (s.indexOf('D') === 0) {
            sum = sum + 500;
            s = s.substring(1)
        } else if (s.indexOf('M') === 0) {
            sum = sum + 1000;
            s = s.substring(1)
        }
    }

    return sum;
}

