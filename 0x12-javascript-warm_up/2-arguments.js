#!/usr/bin/node
const args = process.argv.slice(2);
const argsNum = args.length;
if ((argsNum === 0)) {
  console.log('No argument');
} else if (argsNum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
