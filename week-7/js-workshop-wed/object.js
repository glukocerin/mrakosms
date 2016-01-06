'use strict';

var humwee = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 2e4
};


function ride(car, km) {
  car.km += km
}

ride(humwee, 200);


console.log(humwee.km)

//

var humwee2 = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 2e4,
  ride1: ride1 // vagy ide beirom a fuggvenyt
};


function ride1(km) {
  this.km += km
}

humwee2.ride1(200);


console.log(humwee2.km)
