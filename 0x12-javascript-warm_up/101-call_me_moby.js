#!/usr/bin/node
const callMeMoby = {
  callMeMoby: function (x, theFunc) {
    for (let i = 0; i < x; i++) {
      theFunc();
    }
  }
};
module.exports = callMeMoby;
