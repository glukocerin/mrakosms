function luckCheck(ticket) {
  var first = 0;
  var second = 0;
  for (var i = 0; i < ticket.length / 2; i++ ) {
    first += parseInt(ticket[i])
  }
  for (var i = ticket.length / 2; i < ticket.length; i++ ) {
    second += parseInt(ticket[i])
  }
  if (first === second) {
    return true
  }
  return false;
};
