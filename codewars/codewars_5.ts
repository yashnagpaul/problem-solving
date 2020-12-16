// Given an array containing hashes of names,
// Return a string formatted as a list of names separated by commas
// except for the last two names, which should be separated by an ampersand.

// EXAMPLES:

// list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

// list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

// list([ {name: 'Bart'} ])
// returns 'Bart'

// list([])
// returns ''

function list(names){
    if (names.length<1) return '';
    else if (names.lenth == 1) return names[0].name;
    else {
      let answer = names[0].name;
      for(let i=1;i<=names.length-1;i++){
        names[names.length-1].name == names[i].name ? answer = answer.concat(` & ${names[i].name}`) : answer = answer.concat(`, ${names[i].name}`); 
      }
      return answer;
    }
  }