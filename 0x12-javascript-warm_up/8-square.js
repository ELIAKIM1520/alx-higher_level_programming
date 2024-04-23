#!/usr/bin/node
const ch = 'X';
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += ch;
    }
    console.log(row);
  }
}
