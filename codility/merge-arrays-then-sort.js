// Define a function called merge
// When given two sorted arrays containing numbers,
// the function should return a sorted array of the numbers from both lists.

function merge(arr1, arr2){
    let answer = arr1.concat(arr2)
    return answer.sort((a, b) => a - b);
  }