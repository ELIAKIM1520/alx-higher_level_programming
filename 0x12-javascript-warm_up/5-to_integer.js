#!/usr/bin/node
const array = process.argv.slice(2);
const num = parseInt(array[0]);
console.log(`${isNaN(num) ? 'Not a number' : 'My number: ' + num}`);
