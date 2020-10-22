// Create a function named divisors that takes an integer n > 1 and returns an array
// with all of the integer's divisors from smallest to largest
// (except for 1 and the number itself).
// If the number is prime return the string '(integer) is prime'

function divisors(integer) {
    let divisibles = [];
    let i = 2;
    while (i < integer){
      if(integer % i == 0) divisibles.push(i);
      i++;
    }
    if(divisibles.length>=1) return divisibles; else return `${integer} is prime`;
  };