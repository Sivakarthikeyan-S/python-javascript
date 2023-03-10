thisIsHoisted();
// thisIsNotHoisted(); // error

thisIsAlsoVariable = 'hello';

const thisIsConstant = 5;
// thisIsConstant++; // error
console.log(thisIsConstant);

const constObj = {};
constObj.a = 'a';

let thisIsLet = 51;
thisIsLet = 50;
// let thisIsLet = 51 // errors!
console.log(thisIsLet);

var thisIsVar = 50;
thisIsVar = 51;
var thisIsVar = 500;
console.log(thisIsVar);

function thisIsHoisted() {
    console.log('this is a function declared at the bottom of a file')
}

const thisIsNotHoisted = function() {
    console.log('should this be hoisted?')
}
thisIsNotHoisted();