'use strict';


// var num = 10;
// for (var i = 1; i < num+1; i++) {
//   console.log('----------')
//   for (var j = 1; j < num+1; j++) {
//     var sum = 0;
//     console.log(i + ' x ' + j + ' = ' + i * j);
//   }
// }

// function MultiplicationTable(num) {
//   var output = '';
//   for (var i = 1; i <= num; i++) {
//     var sum = 0;
//     output += i + ' x ' + num + ' = ' + i * num + '\n';
//   }
//   return output
// }

// for (var i = 0; i < 10; i++) {
//   console.log(MultiplicationTable(i));
// }

function MultiplicationTableRecursive(num, i) {
  if (i > 10) {
    return '';
  } else {
    return num + ' x ' + i + ' = ' + num * i + '\n' + MultiplicationTableRecursive(num, i + 1);
  }
}



// return num ? text + textMultiply2(text, num - 1) : '';


console.log(MultiplicationTableRecursive(10, 1));
