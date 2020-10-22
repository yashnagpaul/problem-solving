// Given n, take the sum of the digits of n.
// If that value has more than one digit, continue reducing in this way
// until a single-digit number is produced.
// The input will be a non-negative integer.

function digital_root(n) {
    let arr = Array.from(String(n), Number); // make an array from the user input
    let sum = 0; // initiate sum total
    arr.map(item=>sum+=item); // add up all the values in the array
    while (sum > 9) { // if sum is bigger than a single digit number, reduce it to a single digit number
      let newArr = Array.from(String(sum), Number);
      sum = 0;
      newArr.map(item=>sum+=item);
      }
    return sum;
  }