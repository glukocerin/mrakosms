'use strict';

var num = 65;
var numbers= [];
var Num = String(num);

for (var i = 0; i < Num.length; i++) {
  numbers.push(Num[i]);
}

for (var j = 0; j < num; j++) {
  if (j % 15 === 0 ||
     (String(j).indexOf('3') > -1 && String(j).indexOf('5') > -1)) {
    console.log('fizzbuzz');
  } else if (j % 5 === 0 || String(j).indexOf('5') > -1) {
    console.log('buzz');
  } else if (j % 3 === 0 || String(j).indexOf('3') > -1) {
    console.log('fizz');
  } else {
    console.log(j);
  }
}


