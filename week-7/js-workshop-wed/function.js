'use strict';

function greet(name) {
  console.log('Csá ' + name +'!');
}

greet('Akos');

var koszontes = greet;

koszontes('Gyuri');

var print = console.log;

function greeter (name, log) {
  log('Csovi ' + name);
}

greeter('Lajoskam', print);




function add(a, b) {
  return a + b;
}

var add2 = function (a, b) { return a + b; };

console.log(add2(1, 2));

greeter('Csabi', function(text) {
  console.log(text, 'logged by my function');
})
