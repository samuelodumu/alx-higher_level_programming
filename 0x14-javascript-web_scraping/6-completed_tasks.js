#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];

request(endpoint, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const allTodos = body;
  // console.log(all_todos)
  const newDict = {};
  for (const todo of allTodos) {
    // console.log(todo)
    if (todo.completed) {
      const uid = todo.userId.toString();
      if (uid in newDict) {
        newDict[uid]++;
      } else {
        newDict[uid] = 1;
      }
    }
  }
  console.log(newDict);
});
