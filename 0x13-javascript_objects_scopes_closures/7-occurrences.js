#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let nbo = 0;
  for (const x in list) {
    if (x === searchElement) {
      nbo++;
    }
  }
  return nbo;
}

module.exports = nbOccurences;
