// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
*/
const twoSum = (nums, target) => {
    // initialize an empty array
    let indices = [];

    // i can be our first pointer, j can be our second which is one index ahead of i
    //  we can sum two items at the respective indexes i and j and if they add up to our target number...
    // ...push i and j to our indices array and return it
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums[i].length; j++) {
            if (nums[i] + nums[j] === target) {
                indices.push(i, j);
            }
        }
    }

    return indices;
}