'use strict';

function App () {
  this.model = new Model();
  this.view = new View();
  this.controller = new Controller(this.model, this.view);

}

var todo = new App();

todo.controller.showTasks();
