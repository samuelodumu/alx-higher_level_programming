#!/usr/bin/node

function esrever (list) {
  const newList = []; let x = list.length;
  for (; x > 0; x--) {
    newList.push(list[x - 1]);
  }
  return newList;
}

module.exports = { esrever };
