'use strict';


var kids = [
  {name: 'Julika', age: 8,  sex: 'female'},
  {name: 'Tiborka', age: 7,  sex: 'male'},
  {name: 'Zsolti', age: 6,  sex: 'male'},
  {name: 'Gerda', age: 9,  sex: 'female'},
  {name: 'Zsomborka', age: 8,  sex: 'male'},
]

function countByAge (kids, age) {
  var counter = 0;
  kids.forEach(function (elem) {
    if (elem.age === age) {
      counter++;
    }
  });
  return counter;
}

console.log(countByAge(kids, 8))
