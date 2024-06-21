#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let nbo = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      nbo++;
    }
  }
  return nbo;
}

module.exports = { nbOccurences };
