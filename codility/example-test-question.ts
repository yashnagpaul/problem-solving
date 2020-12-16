// Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0)that does not occur in A.

// For example:
// given A = [1, 3, 6, 4, 1, 2], the function should return 5.
// Given A = [1, 2, 3], the function should return 4.
// Given A = [−1, −3], the function should return 1.

// Write an efficient algorithm for the following assumptions:
// N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].

function solution(A) {
  let ans = 0;
  let positiveArr = A.filter((value) => value > 0);

  for (let i = 0; i < positiveArr.length; i++) {
    let index = positiveArr.indexOf(ans);
    if (index <= 0 && ans > 0) {
      return (ans += 1);
    } else if (index > 0) {
      ans += 1;
    }
  }
  return (ans += 1);
}

solution([1, 3, 6, 4, 1, 2]);
