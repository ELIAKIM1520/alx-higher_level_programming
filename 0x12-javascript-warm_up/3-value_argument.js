#!/usr/bin/node
const array = process.argv.slice(2);
let count = 0;

array.forEach(() => {
  count++;
});
if (count === 0) {
  console.log('No argument');
} else {
  console.log(array[0]);
}
