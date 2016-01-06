'use strict';

// function reverse(string) {
//   var output = '';
//   for (var i = string.length-1; i >= 0; i--) {
//     output += string[i];
//   }
//   return output;
// }



// function reverse(s) {
//   s = s.split('');
//   var len = s.length,
//       halfIndex = Math.floor(len / 2) - 1,
//       tmp;
//   for (var i = 0; i <= halfIndex; i++) {
//     console.log(s);
//     tmp = s[len - i - 1];
//     s[len - i - 1] = s[i];
//     s[i] = tmp;
//   }
//   return s.join('');
// }


function reverse2(input) {
  return reverseRecursive(input, input.length - 1);
}

function reverseRecursive(input, i) {
  if (i < 0) {
    return '';
  } else {
    return input + reverseRecursive(input, i);
  }
}


// console.log(reverse('kacsamajom'));

// console.log(reverseRecursive('kacsamajom', 4));

console.log(reverse2('kacsa'));
