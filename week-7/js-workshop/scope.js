'use strict';

var g = 123;

function printG() {
  console.log(g);
  g = 333;
}

printG();
console.log(g);





function printLocalG() {
  var g = 7;
  console.log(g);
}

printLocalG();
console.log(g);




function printA() {
  var a = 11;
  console.log(a);
}

printA();
// console.log(a); ERROR



{
  var c = 999;
}
console.log(c);



// Block Scope - majd a 6-ost=l

// {
//   let d = 888;
// }
// console.log(d);
