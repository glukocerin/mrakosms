'use strict';

function createTriangle(array) {
  var final_triangle = '';
  array.forEach(function(row, i) {
    final_triangle += Array(array.length-i).join(' ');
    row.forEach(function(e) {
      final_triangle += e + ' ';
    });
    final_triangle += '\n';
  });
  return final_triangle;
}

function pascalTriangle(rows) {
  var triangle = [];
  for (var i = 0; i < rows; i++) {
    var currRow = [];
    var t = triangle.length;
    for (var j = 0; j < t; j++) {
      var prevRow = triangle[t - 1];
      if (typeof prevRow[j - 1] === 'undefined') {
        currRow.push(1);
      } else {
        currRow.push((prevRow[j - 1] + prevRow[j]));
      }
    }
    currRow.push(1);
    triangle.push(currRow);
  }
  return createTriangle(triangle);
}

console.log(pascalTriangle(5));
