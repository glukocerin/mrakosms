'use strict';

var fs = require('fs');

try {
  var content = fs.readFileSync('korte.txt');
} catch (e) {
  content = 'para volt a file-lal'
}
console.log(String(content));
