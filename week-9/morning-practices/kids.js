'use strict';

var kids = [
  {name: 'Julika', age: 8,  sex: 'female'},
  {name: 'Tiborka', age: 7,  sex: 'male'},
  {name: 'Zsolti', age: 6,  sex: 'male'},
  {name: 'Gerda', age: 9,  sex: 'female'},
  {name: 'Zsomborka', age: 8,  sex: 'male'},
]



var getAgeByName = function (kids, name) {
  var age;
  kids.forEach(function (elem) {
    if (elem.name === name) {
      age = elem.age
    }
  });
  return age
}

console.log(getAgeByName(kids, 'Gerda'));
