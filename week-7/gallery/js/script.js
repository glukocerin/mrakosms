'use strict';

var images = [
  {title: '', src: 'images/1.jpg', alt: ''},
  {title: '', src: 'images/2.jpg', alt: ''},
  {title: '', src: 'images/3.jpg', alt: ''},
  {title: '', src: 'images/4.jpg', alt: ''},
  {title: '', src: 'images/6.jpg', alt: ''},
  {title: '', src: 'images/7.jpg', alt: ''},
  {title: '', src: 'images/8.jpg', alt: ''},
  {title: '', src: 'images/9.jpg', alt: ''},
  {title: '', src: 'images/10.jpg', alt: ''},
  {title: '', src: 'images/images_array.png', alt: ''},
  {title: '', src: 'images/functions.png', alt: ''},
  {title: '', src: 'images/event.png', alt: ''},
  {title: '', src: 'images/create_image.png', alt: ''},
  {title: '', src: 'images/create_tn.png', alt: ''},
]

function Gallery(images) {
  var _this = this;
  this.images = images
  this.nextImg = document.querySelector('.next');
  this.prevImg = document.querySelector('.prev');
  this.nextThumb = document.querySelector('.next-tn');
  this.prevThumb = document.querySelector('.prev-tn');
  this.currentImage = document.querySelector('.actual-image');
  this.idxOfImg = 0;
  this.thumbnails = document.querySelector('.thumbnails');
  this.thumbnail = document.querySelector('.thumbnail');

  this.next = function() {
    this.step(images[++this.idxOfImg]);
  }

  this.prev = function() {
    this.step(images[--this.idxOfImg]);
  }

  this.jump = function(event) {
    if (event.target.id) {
      this.idxOfImg = event.target.id;
      this.step(images[this.idxOfImg]);
    }
  }

  this.step = function(image) {
    this.createImage(image)
    this.hideBtn();
  }

  this.createImage = function(image) {
    for (var attr in image) {
      this.createImageAttributes(attr, image[attr]);
    }
    if (this.idxOfImg < 2) {
      this.createThumbnails(2);
    } else if (this.idxOfImg > images.length - 3) {
      this.createThumbnails(images.length - 3);
    } else {
      this.createThumbnails(this.idxOfImg);
    }
    document.getElementById(this.idxOfImg).setAttribute('class', 'active');
  }

  this.createImageAttributes = function(key, value) {
    this.currentImage.setAttribute(key, value);
  }

  this.hideBtn = function() {
    if (this.idxOfImg === 0) {
      this.prevImg.classList.add('hide');
      this.nextImg.setAttribute('src', images[Number(this.idxOfImg) + 1].src);
    } else if (this.idxOfImg === images.length - 1) {
      this.nextImg.classList.add('hide')
      this.prevImg.setAttribute('src', images[Number(this.idxOfImg) - 1].src);
    } else {
      this.prevImg.classList.remove('hide');
      this.nextImg.classList.remove('hide');
      this.prevImg.setAttribute('src', images[Number(this.idxOfImg) - 1].src);
      this.nextImg.setAttribute('src', images[Number(this.idxOfImg) + 1].src);
    }
  }

  this.createThumbnails = function(index) {
    this.thumbnails.innerHTML = '';
    var image;
    var last = Number(index) + 3
    var first = Number(index) - 2
    for (var i = first; i < last; i++) {
      image = document.createElement('img');
      image.setAttribute('id', i);
      image.setAttribute('src', images[i].src);
      image.setAttribute('class', 'thumbnail');
      if (image !== undefined) {
        this.thumbnails.appendChild(image)
      } else {
        break;
      }
    }
  }
  this.createImage(images[++this.idxOfImg])
  this.hideBtn();
  this.nextImg.addEventListener('click', function() {
    _this.next();
  });
  this.prevImg.addEventListener('click', function() {
    _this.prev();
  });
  this.thumbnails.addEventListener('click', function(event) {
    _this.jump(event);
  });

}

var gallery = new Gallery(images);
