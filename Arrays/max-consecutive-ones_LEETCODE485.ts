//Given a binary array, find the maximum number of consecutive 1s in this array.

// Example:
// Input: [1,1,0,1,1,1]
// Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s.
// The maximum number of consecutive 1s is 3.

// Note:
// The input array will only contain 0 and 1.
// The length of input array is a positive integer and will not exceed 10,000

var findMaxConsecutiveOnes = function(nums) {
    let i = 0;
    let oneCounter = 0;
    let currentHighest = 0;
    while (i < nums.length) {
       if (nums[i] == 1){
           oneCounter+=1;
            currentHighest < oneCounter ? currentHighest = oneCounter : '';
        }
        else {
            currentHighest < oneCounter ? currentHighest = oneCounter : '';
            oneCounter=0;
        }
        i++;
    }
    return currentHighest;
};