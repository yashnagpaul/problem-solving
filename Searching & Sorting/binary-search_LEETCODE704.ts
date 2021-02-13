// Given a sorted (in ascending order) integer array nums of n elements and a target value,
// write a function to search target in nums.
// If target exists, then return its index, otherwise return -1.


var search = function(nums, target) {

  let left = 0;
  let right = nums.length - 1;
  let pivot = nums.length % 2 == 0 ? nums.length / 2 : (nums.length + 1) / 2;
  
  while (left <= right) {
    
    if (nums[pivot] == target) {
      return pivot;
    }
    
    else if (target > nums[pivot]){
      left = pivot + 1;
    }
    
    else if (target < nums[pivot]){
      right = pivot - 1;
    }
    
    pivot = (right + left) % 2 == 0 ? (right + left) / 2 : (right + left + 1) / 2;
  }
  
  return -1
};
