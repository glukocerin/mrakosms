'use strict';


for (var i = 0; i < 12; i += 3) {
  console.log(i);
}

var dogs = ['Virsli', 'Tappancs', 'Morzsi'];

for (var i = 0; i < dogs.length; i++) {
  console.log(dogs[i]);
}



// ONLY OBJEKTUM "FOR" !!!

var student = {
  kor: 6,
  nev: 'tibi',
  labmeret: 42
};

for (var key in student) {
  console.log(key + ': ' + student[key]);
}
