#!/usr/bin/node
const fs = require('fs');

const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];

fs.readFile(src1, 'utf8', (err, data) => {
  if (err) {
    console.error(`Error reading  ${src1}: ${err}`);
    return;
  }

  fs.readFile(src2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${src2}: ${err}`);
      return;
    }
    const concatData = data + data2;

    fs.writeFile(dest, concatData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${dest}: ${err}`);
      }
    });
  });
});
