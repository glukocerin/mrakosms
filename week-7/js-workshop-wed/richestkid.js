'use strict';

var kids = [
  {name: 'Tibbor', candies: 20},
  {name: 'Steve', candies: 3},
  {name: 'Agoston', candies: 12},
  {name: 'Julika', candies: 37},
  {name: 'Krisztian', candies: 4},
  ];


function getRichestKidsName(kids) {
  var richestKid = kids[0];
  var i = 1;
  for (var i = 0; i < kids.length; i++) {
    var currentKid = kids[i];
    if (richestKid.candies < currentKid.candies) {
      richestKid = currentKid;
    }
  }
  return richestKid.name;
}

function getRichestKidsName2(kids) {
  var richestKid = kids[0];
  kids.forEach(function(currentKid) {
    if (richestKid.candies < currentKid.candies) {
      richestKid = currentKid;
    }
  });
  return richestKid.name
}

function getRichestKidsName3(kids) {


}

//   kids.reduce(function(richest, i) {
//     richest = richest > kids[i].candies ? richest : kids[i].candies;
//   });
//   return richest
// }

console.log(getRichestKidsName(kids));
console.log(getRichestKidsName2(kids));
console.log(getRichestKidsName3(kids));
