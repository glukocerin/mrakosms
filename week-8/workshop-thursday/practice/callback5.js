'use strict';

var fs = require('fs');

function countLetterP (callback) {
  fs.readFile('alma.txt', function(err, content) {
    var stringContent = String(content);
    var count = 0;
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i].toUpperCase() === 'P') {
        count++;
      }
    }
    callback(count);
  });
}

countLetterP(function (count) {
  console.log(count)
});
