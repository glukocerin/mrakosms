'use strict';

// Nagybetuvel Constructor fv

function Car(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;
  this.ride = function(km) { this.km += km; }
}

var golf = new Car('kopott piros', '1-es Golf', 1e10);

golf.ride(400);

console.log(golf.km)
