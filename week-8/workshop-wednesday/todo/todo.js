'use strict';

var probaRequest = new XMLHttpRequest();

function Model () {

}

function View () {

}

function Controller () {


  this.addItem = function () {

  }

  this.saveItem = function () {

  }

  this.completeItem = function () {

  }

 }




function createRequest(url, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.send();
  probaRequest.onreadystatechange = function () {
  console.log('state: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var todoContainer = document.querySelector('.todo-container');

var todoCallback = function(response) {
  console.log(JSON.parse(response));
  var todoArray = JSON.parse(response);
  todoArray.forEach(function (todoItem) {
    console.log(todoItem.text);
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  });
}



function sendItem() {
  var req = new XMLHttpRequest();
  req.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  req.setRequestHeader('Content-Type', 'application/json')
  req.send(JSON.stringify({text: 'Ki jon cigizni?'}));
}

// sendItem();

createRequest(url, todoCallback);
