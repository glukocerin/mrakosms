'use strict';

function triangle(num) {
  var output = ''
  for (var i = 1; i <= num; i++) {
    var empty = Array(num-i+1).join(' ');
    var hashmarks = Array(i*2).join('#');
    output += empty + hashmarks + empty + '\n';
  }
  return output;
}

console.log(triangle(3));
console.log(triangle(5));
