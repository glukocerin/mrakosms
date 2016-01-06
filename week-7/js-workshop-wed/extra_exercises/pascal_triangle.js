'use strict';

function createTriangle(array) {
  var output = '';
  array.forEach(function(row, i) {
    output += Array(array.length-i).join(' ');
    row.forEach(function(e) {
      output += e + ' ';
    });
    output += '\n';
  });
  return output;
}

function pascalTriangle(rows) {
  var triangle = [];
  for (var i = 0; i < rows; i++) {
    var curr = [];
    triangle.forEach(function(e, j) {
      var prev = triangle[triangle.length - 1];
      !!prev[j - 1] ? curr.push((prev[j - 1] + prev[j])) : curr.push(1);
    });
    curr.push(1);
    triangle.push(curr);
  }
  return createTriangle(triangle);
}

console.log(pascalTriangle(5));
