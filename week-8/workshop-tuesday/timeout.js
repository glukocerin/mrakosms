'use strict';


var isEnd = false;
setTimeout(function() {
  console.log('JEJ!');
  isEnd = true;
}, 1000);


function end() {
  console.log('END');
  console.log('END2');
}


end();
