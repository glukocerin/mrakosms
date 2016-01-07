'use strict';

console.log('mukodik');


var cim = document.querySelector('.majom');

console.log(cim);
cim.classList.add('piros');

var majomKep = document.querySelector('img');

majomKep.setAttribute('src', 'https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg');

var bodyvaltozoban = document.querySelector('body');

function kepcsinalo(src) {
  var newImg = document.createElement('img');
  newImg.setAttribute('src',src);
  bodyvaltozoban.appendChild(newImg);
}

var kepek = ['http://kep.cdn.index.hu/1/0/1053/10532/105324/10532411_337425_ecb22ead25db711158129cc8ceca4265_wm.jpg',
'http://kep.cdn.index.hu/1/0/1075/10756/107569/10756999_354409_1ba477a5d4444e050640cf75c2cf759a_wm.jpg',
'http://kep.cdn.index.hu/1/0/1075/10758/107586/10758651_354529_760a24e9fc4638fa4736247bb0a3e4c8_wm.jpg',
'http://kep.cdn.index.hu/1/0/1075/10756/107562/10756247_354323_f2c02db53909cf26dc2570c9eb79bc91_wm.jpg',
'http://kep.cdn.index.hu/1/0/1075/10758/107584/10758469_354515_2b275aae545ae3794f767138f7ce9378_wm.jpg',
'http://kep.cdn.index.hu/1/0/893/8931/89317/8931795_220523_d3b6a936b0b4ec36c00e37ab1f8558be_wm.jpg', 'http://kep.cdn.index.hu/1/0/1076/10760/107603/10760363_354625_e89e6090f55b1d425ad9df5acc0a0da5_wm.jpg',
'http://kep.cdn.index.hu/1/0/1073/10733/107332/10733261_352751_d7784efd97259fc9612accf662f7a7b6_wm.jpg',
'http://kep.cdn.index.hu/1/0/1075/10755/107553/10755317_354277_a2f68d0f40801a23f515f15ce506dfcd_wm.png',
'http://kep.cdn.index.hu/1/0/1075/10755/107554/10755435_354283_8f817d3f6ae05e505244a87a406ae422_wm.jpg',
'http://kep.cdn.index.hu/1/0/1076/10760/107603/10760345_354623_95385d6731892e28010584223f4c6c12_wm.jpg']

// kepek.forEach(function(src) {
//   kepcsinalo(src);
// })


var gomb = document.querySelector('.csinal');

gomb.addEventListener('click',
  function() {
    kepcsinalo('http://kep.cdn.index.hu/1/0/893/8931/89317/8931795_220523_d3b6a936b0b4ec36c00e37ab1f8558be_wm.jpg', 'http://kep.cdn.index.hu/1/0/1076/10760/107603/10760363_354625_e89e6090f55b1d425ad9df5acc0a0da5_wm.jpg')
  });



window.addEventListener('scroll',
  function() {
    console.log('scroll');
    console.log(window.scrollY);
  })

// cica kutya valto

var cicagomb = document.querySelector('.cicat');
var kutyagomb = document.querySelector('.kutyat');
var valtoskep = document.querySelector('.kepvalto');


kutyagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'http://www.barathegyisegitokutya.hu/wp-content/uploads/2014/09/kutya_egeszsegvedelme.jpg')
});

kutyagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'https://media.giphy.com/media/vhsNmFjuN4WDS/giphy.gif')
});
