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

var nextBtn = document.querySelector('.next');
var prevBtn = document.querySelector('.prev');
var nextImg = document.querySelector('.next-image');
var prevImg = document.querySelector('.prev-image');
var nextThumb = document.querySelector('.next-tn');
var prevThumb = document.querySelector('.prev-tn');
var currentImage = document.querySelector('.actual-image');
var idxOfImg = 0;
var thumbnails = document.querySelector('.thumbnails');
var thumbnail = document.querySelector('.thumbnail');

function next() {
  step(images[++idxOfImg]);
}

function prev() {
  step(images[--idxOfImg]);
}

function jump() {
  if (event.target.id) {
    idxOfImg = event.target.id;
    step(images[idxOfImg]);
  }
}

function step(image) {
  createImage(image)
  hideBtn();
}

function createImage(image) {
  for (var attr in image) {
    createImageAttributes(attr, image[attr]);
  }
  if (idxOfImg < 2) {
    createThumbnails(2);
  } else if (idxOfImg > images.length - 3) {
    createThumbnails(images.length - 3);
  } else {
    createThumbnails(idxOfImg);
  }
  document.getElementById(idxOfImg).setAttribute('class', 'active');

}

function createImageAttributes(key, value) {
  currentImage.setAttribute(key, value);
}

function hideBtn() {
  if (idxOfImg === 0) {
    prevBtn.classList.add('hide');
    nextImg.setAttribute('src', images[Number(idxOfImg) + 1].src);
  } else if (idxOfImg === images.length - 1) {
    nextBtn.classList.add('hide')
    prevImg.setAttribute('src', images[Number(idxOfImg) - 1].src);
  } else {
    prevBtn.classList.remove('hide');
    nextBtn.classList.remove('hide');
    prevImg.setAttribute('src', images[Number(idxOfImg) - 1].src);
    nextImg.setAttribute('src', images[Number(idxOfImg) + 1].src);
  }
}

function createThumbnails(idxOfImg) {
  thumbnails.innerHTML = '';
  var image;
  var last = Number(idxOfImg) + 3
  var first = Number(idxOfImg) - 2
  for (var i = first; i < last; i++) {
    image = document.createElement('img');
    image.setAttribute('id', i);
    image.setAttribute('src', images[i].src);
    image.setAttribute('class', 'thumbnail');
    if (image !== undefined) {
      thumbnails.appendChild(image)
    } else {
      break;
    }
  }
}

createImage(images[idxOfImg])
hideBtn();

nextBtn.addEventListener('click', next);
prevBtn.addEventListener('click', prev);
thumbnails.addEventListener('click', jump);



