'use strict';

function CandiesGame(candiesPerLollipop, lollipopsPerSpeed, end) {
  this.cPL = candiesPerLollipop;
  this.lPS = lollipopsPerSpeed;
  this.candies = 0;
  this.lollipops = 0;
  this.speed = 0;
  this.end = end;
  var _this = this;

  this.updateCandiesDisplay = function() {
    this.updateDisplay('.candies',this.candies);
  }

  this.updateLollipopDisplay = function() {
    this.updateDisplay('.lollipops',this.lollipops);
  }

  this.updateSpeedpDisplay = function() {
    this.updateDisplay('.speed',this.speed);
  }

  this.updateDisplay = function(classname, newHtml) {
    document.querySelector(classname).innerHTML = newHtml;
  }

  this.buyLollipop = function(num) {
    this.candies -= this.cPL * Number(num);
    this.lollipops += Number(num);
    document.getElementById('lollipop').value = '1';
    }

  this.buyLollipopVisibility = function() {
    var buydiv = document.querySelector('.buy');
    if (this.candies >= this.cPL) {
      buydiv.classList.remove('hidden');
    } else {
      buydiv.classList.add('hidden');
    }
    this.setMaxBuyLollipop();
  }

  this.setMaxBuyLollipop = function() {
    var maximum = Math.floor(this.candies / this.cPL);
    document.getElementById('lollipop').max = maximum;
    document.querySelector('.lollipop-max').innerHTML = 'Buy the max: ' + maximum;
    return maximum;
  }

  this.setUpdateInterval = function() {
    this.getSpeed();
    if (this.speed >= 1 && this.speed <= 20) {
      clearInterval(this.newInterval);
      this.newInterval = setInterval(function() {
        _this.updatePageAfterCandies();
      }, _this.setTimeInterval());
    }
  }

  this.getSpeed = function() {
    this.speed = Math.floor(this.lollipops / this.lPS);
    this.updateSpeedpDisplay();
  }

  this.setTimeInterval =function() {
    var time = 1000;
    return time / this.speed;
  }

  this.updatePageAfterCandies = function() {
    this.candies ++;
    this.updateCandiesDisplay();
    this.buyLollipopVisibility();
    this.theEnd();
  }

  this.updatePageAfterLollipop = function(value) {
    this.buyLollipop(value);
    this.updateCandiesDisplay();
    this.updateLollipopDisplay();
    this.buyLollipopVisibility();
    this.setUpdateInterval();
  }

  this.theEnd = function() {
    if (this.candies === this.end) {
      clearInterval(this.newInterval);
      alert('You WIN!!!');
      this.candies = 0;
      this.lollipops = 0;
    }
  }

  this.main = function() {
    document.querySelector('.candy').addEventListener('click', function() {
        _this.updatePageAfterCandies();
      });

    document.querySelector('.lollipop').addEventListener('click', function() {
        _this.updatePageAfterLollipop(document.getElementById('lollipop').value);
      });

    document.querySelector('.lollipop-max').addEventListener('click', function() {
        _this.updatePageAfterLollipop(_this.setMaxBuyLollipop());
      });
  }
}

var game = new CandiesGame(5, 2, 10);
game.main();


