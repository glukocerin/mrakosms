'use strict';

var count = 0;

var interval = setInterval(function() {
  count++;
  console.log(count)
}, 500);


setTimeout(function() {
  console.log('Boom');
  clearInterval(interval);
}, 5000);

