'use strict';

function arabic2roman(arabic) {
  var result = '';
  var tokens = {M : 1000, CM : 900, D : 500, CD : 400, C : 100, XC : 90, L : 50, XL : 40, X : 10, IX : 9, V : 5, IV : 4, I : 1}
  while (arabic > 0) {
    for (var key in tokens) {
      if (tokens[key] <= arabic) {
        result += key;
        arabic -= tokens[key];
        break;
      }
    }
  }
  return result
}

module.exports = arabic2roman;
