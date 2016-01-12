'use strict';

function CandiesGame() {
  this.candies = 0;
  this.lollipops = 0;
  this.speed = 0;
  this.candiesPerLollipop = 10;
  this.lollipopsPerSpeed = 2;

  this.selectCreateCandy = document.querySelector('.create-candy');
  this.selectBuyLollipop = document.querySelector('.buy-lollipop');
  this.selectCandies = document.querySelector('.candies');
  this.selectLollipops = document.querySelector('.lollipops')
  this.selectSpeed = document.querySelector('.speed')
  this.selectLollipopNumber = document.querySelector('.lollipop-number')
  this.selectLollipopForm = document.querySelector('.lollipop-form')
  var _this = this

  this.growCandies = function() {
    this.candies++;
    this.selectCandies.innerHTML = this.candies;
    this.changeButtonVisibility();
  }

  this.buyLollipop = function(num) {
    num = Number(num);
    if (this.candies >= this.candiesPerLollipop) {
      this.candies -= this.candiesPerLollipop * num;
      this.lollipops += num;
      this.selectCandies.innerHTML = this.candies;
      this.selectLollipops.innerHTML = this.lollipops;
      this.getSpeed();
      document.getElementById('hello').value = '1';
      this.changeButtonVisibility();
    }
  }


  this.changeButtonVisibility = function() {
    this.selectBuyLollipop.disabled = true;
    this.selectLollipopNumber.disabled = true;
    this.selectLollipopForm.classList.add('class', 'hidden')
    if (this.candies >= this.candiesPerLollipop) {
      this.selectBuyLollipop.disabled = false;
      this.selectLollipopForm.classList.remove('class', 'hidden')
      this.selectLollipopNumber.disabled = false;

      this.selectLollipopNumber.setAttribute('max', Math.floor(this.candies / this.candiesPerLollipop));
    }
  }

  this.getSpeed = function() {
    this.speed = Math.floor(this.lollipops / this.lollipopsPerSpeed);
    this.selectSpeed.innerHTML = this.speed;
    if (this.speed >= 1 && this.speed <= 20) {
      clearInterval(this._interval);
      this._interval = setInterval(function() {
        _this.candies ++;
        _this.selectCandies.innerHTML = _this.candies;
        _this.changeButtonVisibility();
      }, 1000/_this.speed);
      this.theEnd();
    }
  }

  this.theEnd = function() {
    if (this.candies >= 1000) {
      clearInterval(_interval);
      candies = 0;
      lollipops = 0;
      alert('You Win');
    }
  }

  this.selectCreateCandy.addEventListener('click', function() {
      _this.growCandies();
    });

  this.selectBuyLollipop.addEventListener('click', function() {
      _this.buyLollipop(_this.selectLollipopNumber.value);
    });

}

var game = new CandiesGame();

