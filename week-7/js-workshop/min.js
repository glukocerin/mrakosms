'use strict';

var numbers = [7, 8, -1, 4, -3, 12];
var actualMin = Infinity;

for (var i = 0; i < numbers.length; i++) {
  // actualMin = numbers[i] < actualMin ? numbers[j] : actualMin
  if (numbers[i] < actualMin) {
    actualMin = numbers[i];
  }
}

console.log(actualMin);

