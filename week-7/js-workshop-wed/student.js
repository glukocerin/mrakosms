'use strict';

function Student(name) {
  this.name = name;
  this.grades = [];
  this.addGrade = function(grade) {
    this.grades.push(grade);
  }
  this.getAverage = function () {
      return this.grades.reduce(function (acc, num) {
        return acc + num;
      }, 0) / this.grades.length;
  }
}

var jozsi = new Student('Jozsef');
jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);

console.log(jozsi.getAverage());
