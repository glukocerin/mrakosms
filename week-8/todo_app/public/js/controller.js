'use strict';

function Controller (model, view) {
  this.model = model;
  this.view = view;
  var _this = this;
  this.ENTER_KEY = 13;
  var container = document.querySelector('.container');
  var addButton = document.querySelector('.add');

  this.showTasks = function () {
    this.model.getTasks(this.view.showTasks);
  }

  this.addTask = function () {
    var newTask = document.querySelector(".new-task").value;
    if (newTask !== '') {
      _this.model.createTask(newTask, _this.view.addTask);
    }
  }

  this.editTask = function (id) {
    _this.model.getTask(id, _this.view.editTask);
  }

  this.updateTask = function (id, text, status) {
    _this.model.updateTask(id, text, status, _this.view.updateTask);
  }

  this.updateToggle = function (id, text, status) {
    _this.model.updateTask(id, text, status, _this.view.taskToggle);
  }

  this.deleteTask = function (id) {
    _this.model.deleteTask(id, _this.view.deleteTask);
  }

  addButton.addEventListener('click', this.addTask);

  container.addEventListener('click', function (event) {
    if (event.target.className === 'delete') {
        _this.deleteTask(event.target.parentNode.id);
    }
    if (event.target.className === 'edit') {
        _this.editTask(event.target.parentNode.id);
    }
    if (event.target.className === 'done') {
      var id = event.target.parentNode.id;
      var status = event.target.parentNode.children[0].checked
      var text = event.target.parentNode.children[2].value
        _this.updateTask(id, text, status);
    }
   }, false);

  container.addEventListener('change', function (event) {
    if (event.target.type === 'checkbox') {
      var id = event.target.parentNode.id;
      var status = event.target.parentNode.children[0].checked
      var text = event.target.parentNode.children[1].innerHTML
        _this.updateToggle(id, text, status);
    }
  }, false);
}
