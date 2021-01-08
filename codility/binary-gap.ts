// Question:
// Given a positive integer n, find and return the longest distance
// between any two adjacent 1's in the binary representation of n.
// If there are no two adjacent 1's, return 0.

function binaryGap(n: number): number {
    
  let zCount = 0;
  let maxGap = 0;
  let foundFirstOne = false;
  let foundSecondOne = false;
  let binary = n.toString(2);
  
  for (let i = 0; i < binary.length; i++) {
      if (binary[i] == "0"){
          zCount+=1;
      }
      else {
          foundFirstOne == false ? foundFirstOne = true : foundSecondOne = true;
          if (foundFirstOne && foundSecondOne && maxGap < zCount) {
              maxGap = zCount; 

          }
          zCount = 0; 
      }
  }
  return foundFirstOne && foundSecondOne ? maxGap+1 : maxGap;
};

// Explanation:
// the loop iterates through the binary format of the number
// if the current digit is "0" we increase our zero counter by 1

// otherwise, we check whether we have come across at least two ones ("1")
// if so, we also check whether our current running count of zeroes is
// higher than what we stored in maxGap, which tracks the value for most consecutive zeroes

// if all these conditions are met, we assign the value of zCount to maxGap
// before the next iteration of the loop, we make sure to reset the zero count

// finally, if the binary format had at least two ones ("1"),
// we add 1 to our count of maximum consecutive zeroes and return that value
// if the binary format didn't have at least two ones,
// we simply return the value of maxGap, which will be 0 in that case.
