// Function Description
// Complete the aVeryBigSum function.
// It must return the sum of all array elements.

// aVeryBigSum has the following parameter(s):
// int ar[n]: an array of integers .

// Return
// long: the sum of all array elements

function aVeryBigSum(ar) {
    let total = 0;
    ar.forEach(item => total+=item);
    return total;
    }
    