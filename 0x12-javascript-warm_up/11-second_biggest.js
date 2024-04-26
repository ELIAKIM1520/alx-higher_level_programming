#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const len = args.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secMax = -Infinity;

  for (const num of args) {
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num > secMax && num !== max) {
      secMax = num;
    }
  }
  console.log(secMax);
}
