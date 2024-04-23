#!/usr/bin/node
const arg = parseInt(process.argv[2]);
function recursion (num) {
  if (isNaN(num)) return 1;
  if (num <= 1) {
    return 1;
  } else {
    return num * recursion(num - 1);
  }
}
console.log(recursion(arg));
