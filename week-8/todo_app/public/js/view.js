'use strict';

function View () {
  var _this = this;
  this.incompleteTasks = document.getElementById("incomplete-tasks");
  this.completedTasks = document.getElementById("completed-tasks");

  this.template = function (id, text, status) {
    var taskHolder = document.createElement('li');
    var checkBox = document.createElement('input');
    var label = document.createElement('label');
    var editInput = document.createElement('input');
    var editButton = document.createElement('button');
    var deleteButton = document.createElement('button');

    checkBox.type = "checkbox";
    editInput.type = "text";
    editButton.innerText = 'Edit';
    editButton.className = "edit";
    deleteButton.innerText = 'Delete';
    deleteButton.className = "delete";

    taskHolder.appendChild(checkBox);
    taskHolder.appendChild(label);
    taskHolder.appendChild(editInput);
    taskHolder.appendChild(editButton);
    taskHolder.appendChild(deleteButton);

    taskHolder.setAttribute("id", id);

    label.innerText = text;
    checkBox.checked = status;

    return taskHolder;
  }


  this.showTasks = function (data) {
    for (var i = data.length-1; i >= 0; i--) {
      var task = _this.template(data[i].id, data[i].text, data[i].completed)
      if (data[i].completed) {
        _this.completedTasks.appendChild(task);
      } else {
        _this.incompleteTasks.appendChild(task);
      }
    }
  }

  this.addTask = function (data) {
    var task = _this.template(data.id, data.text, data.completed);
    _this.incompleteTasks.insertBefore(task, _this.incompleteTasks.childNodes[0]);
    document.querySelector(".new-task").value = '';
  }

  this.editTask = function (data) {
    var task = document.getElementById(data.id)
    var editInput = task.querySelector("input[type=text");
    var label = task.querySelector("label");
    var editButton = task.querySelector(".edit");
    task.classList.add("editMode");
    editButton.innerText = 'Done';
    editButton.className = "done";
    editInput.value = label.innerText;
  }

  this.updateTask = function (data) {
    var task = document.getElementById(data.id)
    var editInput = task.querySelector("input[type=text");
    var label = task.querySelector("label");
    var editButton = task.querySelector(".done");
    task.classList.remove("editMode");
    editButton.innerText = 'Edit';
    editButton.className = "edit";
    label.innerText = editInput.value;
  }

  this.deleteTask = function (data) {
    var task = document.getElementById(data.id);
    task.remove();
  }

  this.taskToggle = function(data) {
    var task = document.getElementById(data.id);
    if (data.completed === true) {
      task.remove();
      _this.completedTasks.appendChild(task);
    } else {
      task.remove();
      _this.incompleteTasks.appendChild(task);
    }
  }
}
