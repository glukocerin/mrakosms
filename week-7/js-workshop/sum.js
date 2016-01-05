'use strict';


function sumNumber(list) {
  var sum = 0;
  for (var i = 0; i <list.length; i++) {
    sum += list[i];
  }
  return sum;
}


console.log(sumNumber([1, 2, 3]));
console.log(sumNumber(['w', 2]));
console.log(sumNumber([1, 2, 3, 4]));

function sum2(list) {
  var total = list.reduce(function(a, b) {return a + b;});
  return total;
}

console.log(sum2([1, 2, 3, 4, 5]));
