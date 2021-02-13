// Usually when you buy something, you're asked whether your credit card number,
// phone number or answer to your most secret question is still correct.
// However, since someone could look over your shoulder,
// you don't want that shown on your screen. Instead, we mask it.

// Your task is to write a function maskify, which changes all but the last four characters into '#'.

// return masked string
function maskify(cc) {
    const length=cc.length; // get the length of the CC
    const finalFourDigits=`${cc[length-4]}${cc[length-3]}${cc[length-2]}${cc[length-1]}`;
    if(length>4){
      return ("#".repeat(length-4))+finalFourDigits;
    }
    else return cc;
  }
  