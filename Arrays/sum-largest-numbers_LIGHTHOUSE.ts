// In this exercise, we will be given an array of 2 or more numbers.
// We will then have to find the two largest numbers in that array, and sum them together.

const sumLargestNumbers = function (data) {
  let largest = 0;
  let secondLargest = 0;
  for (let i = 0; i < data.length; i++) {
    if (data[i] > largest) {
      largest = data[i];
    }
  }
  for (let i = 0; i < data.length; i++) {
    if (data[i] > secondLargest && data[i] < largest) {
      secondLargest = data[i];
    }
  }
  let sum = largest + secondLargest;
  return sum;
};

console.log(sumLargestNumbers([1, 10])); //returns 11 (example)
console.log(sumLargestNumbers([1, 2, 3])); //returns 5 (example)
console.log(sumLargestNumbers([10, 4, 34, 6, 92, 2])); //returns 126 (example)