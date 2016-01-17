'use strict';

var fs = require('fs')

function getFirstIndexInAlmaTxt(letter, callback) {
  fs.readFile('alma.txt', function(err, content) {
    if (err) {
      return callback(err);
    }
    var stringContent = String(content);
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i] === letter) {
        return callback(err, i);
      }
    }
  });
}



getFirstIndexInAlmaTxt('p', function (err, index) {
  console.log(index);
});
