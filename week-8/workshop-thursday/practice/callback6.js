'use strict';

var fs = require('fs');

function countLetterInAlmaTxt (char, callback) {
  fs.readFile('alma.txt', function(err, content) {
    var stringContent = String(content);
    var count = 0;
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i].toUpperCase() === char.toUpperCase()) {
        count++;
      }
    }
    callback(count);
  });
}

countLetterInAlmaTxt('p', function (count) {
  console.log(count);
});
