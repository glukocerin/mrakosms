'use strict';

function Model () {
  this.url = 'http://localhost:3000/todos/';
  var _this = this;

  this.createRequest = function (method, url, data, cb) {
    var req = new XMLHttpRequest();
    req.open(method, url);
    req.setRequestHeader('Content-Type', 'application/json');
    req.send(data);
    req.onreadystatechange = function () {
      if (req.readyState === 4) {
        var res = JSON.parse(req.response);
        return cb(res);
      }
    };
  }

  this.getTasks = function (cb) {
    return this.createRequest('GET', this.url, {}, cb);
  }

  this.getTask = function (id, cb) {
    var url = this.url + id;
    return this.createRequest('GET', url, {}, cb);
  }

  this.createTask = function (text, cb) {
    var data = JSON.stringify({ "text": text });
    return this.createRequest('POST', this.url, data , cb);
  }

  this.updateTask = function (id, text, status, cb) {
    var url = this.url + id;
    var data = JSON.stringify({ "text": text, "completed": status });
    return this.createRequest('PUT', url, data , cb);
  }

  this.deleteTask = function (id, cb) {
    var url = this.url + id;
    return this.createRequest('DELETE', url, null, cb);
  }
}
