'use strict';

var arabic2roman = require('./kata')
var tape = require('tape');

tape('roman converter', function(t) {
  t.equal(arabic2roman(0), '');
  t.equal(arabic2roman(1), 'I');
  t.equal(arabic2roman(2), 'II');
  t.equal(arabic2roman(3), 'III');
  t.equal(arabic2roman(4), 'IV');
  t.equal(arabic2roman(5), 'V');
  t.equal(arabic2roman(6), 'VI');
  t.equal(arabic2roman(7), 'VII');
  t.equal(arabic2roman(8), 'VIII');
  t.equal(arabic2roman(9), 'IX');
  t.equal(arabic2roman(10), 'X');
  t.equal(arabic2roman(11), 'XI');
  t.equal(arabic2roman(14), 'XIV');
  t.equal(arabic2roman(15), 'XV');
  t.equal(arabic2roman(19), 'XIX');
  t.equal(arabic2roman(20), 'XX');
  t.equal(arabic2roman(40), 'XL');
  t.equal(arabic2roman(90), 'XC');
  t.equal(arabic2roman(100), 'C');
  t.equal(arabic2roman(110), 'CX');
  t.equal(arabic2roman(111), 'CXI');
  t.equal(arabic2roman(500), 'D');
  t.equal(arabic2roman(900), 'CM');
  t.equal(arabic2roman(1000), 'M');
  t.equal(arabic2roman(3888), 'MMMDCCCLXXXVIII');
  t.end();
});
