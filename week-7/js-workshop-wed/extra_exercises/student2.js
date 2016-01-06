'use strict';

function Student() {
  this.grades = {};
  this.addGrade = function (subject, grade) {
    if (subject in this.grades) {
      this.grades[subject].push(grade);
    } else {
      this.grades[subject] = [grade];
    }
  }
  this.getCount = function () {
    var output = {};
    for (var key in this.grades) {
      output[key] = this.grades[key].length;
    }
    return output;
  }

  this.getAverage = function () {
    var gradesSum = 0;
    var counter = 0;
    for (var key in this.grades) {
      this.grades[key].forEach(function(e) {
        gradesSum += e;
        counter += 1;
      });
    }
    return (gradesSum / counter).toFixed(2);
  }

  this.getAverageBySubject = function() {
    var gradesAvg = {}
    for (var key in this.grades) {
      gradesAvg[key] = (this.grades[key].reduce(function (acc, grade) {
      return acc + grade;
      }, 0) / this.grades[key].length).toFixed(2);
    }
    return gradesAvg;
  }
}

var dezso = new Student();
dezso.addGrade('matek',5);
dezso.addGrade('matek',4);
dezso.addGrade('matek',5);
dezso.addGrade('rajz',1);
dezso.addGrade('rajz',3);
console.log('Num of grades:', dezso.getCount()); // {rajz: 2, matek: 3} // hany jegyet kapott
console.log('Total avg:',dezso.getAverage()); // 3.4
// // szorg
console.log('Avg of subjets:',dezso.getAverageBySubject()); // {matek: 4.3}
