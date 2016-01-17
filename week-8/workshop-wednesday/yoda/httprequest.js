'use strict';
var ACCESS_TOKEN = 'UtGiWjrI4DmshZSWQ0F2Slt9s8jdp1LeHnEjsntSEbctZll7Py';



function createRequest(url, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);
  probaRequest.send();
  probaRequest.onreadystatechange = function () {
  console.log('state: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

var responseContainer = document.querySelector('.yoda-response');

function onDone(response) {
    responseContainer.innerText = response;
    console.log('Response: ', response);
}

var yodaButton = document.querySelector('.yoda-button');
var yodaInput = document.querySelector('.yoda-input');

yodaButton.addEventListener('click', function() {
  var url = 'https://yoda.p.mashape.com/yoda';
  var sentence = yodaInput.value;
  var urlWithParams = url + '?sentence=' + encodeURIComponent(sentence);

  responseContainer.innerText = 'loading...'
  createRequest(urlWithParams, onDone);
});
