'use strict';

function textMultiply(string, num) {
  var multiWord = '';
  for (var i = 0; i < num; i++) {
    multiWord += string;
  }
  return multiWord;
}

console.log(textMultiply('alma', 3));

var multiWord = '';

function textMultiply2(text, num) {
  return num ? text + textMultiply2(text, num - 1) : '';
}

function textMultiply3(text, num) {
  if (num === 0) {
    return '';
  } else {
    return text + textMultiply3(text, num - 1);
  }
}

console.log(textMultiply2('alma', 3));
console.log(textMultiply3('alma', 4));
