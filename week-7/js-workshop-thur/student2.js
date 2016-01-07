'use strict';

function Student() {
  this.grades = [];
  this.addGrade = function (subject, grade) {
    this.grades.push({subject: subject, grade: grade})
  };
  this.getCount = function () {
    var output = {};
    this.grades.forEach(function(grade) {
      !!output[grade.subject] ? output[grade.subject]++ : output[grade.subject] = 1;
    });
    return output;
  };
}



var dezso = new Student();
dezso.addGrade('matek',5);
dezso.addGrade('matek',4);
dezso.addGrade('matek',5);
dezso.addGrade('rajz',1);
dezso.addGrade('rajz',3);

console.log('Num of grades:', dezso.getCount());

