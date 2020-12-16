// Given the array candies and the integer extraCandies,
// where candies[i] represents the number of candies that the ith kid has.

// For each kid check if there is a way to distribute extraCandies among the kids
// such that he or she can have the greatest number of candies among them.
// Notice that multiple kids can have the greatest number of candies.

// EXAMPLE
// Input: candies = [12,1,12], extraCandies = 10
// Output: [true,false,true]

let kidsWithCandies = function(candies, extraCandies) {
    let answerArr = [];
    for (let i=0; i < candies.length; i++){
        (candies[i] + extraCandies) >= Math.max(...candies) ? answerArr.push(true) : answerArr.push(false);
    }
    return answerArr;
};