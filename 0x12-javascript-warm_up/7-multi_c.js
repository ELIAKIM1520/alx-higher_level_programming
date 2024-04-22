#!/usr/bin/node

const myVar = "C is fun";

if (process.argv[2]) {
    const number = parseInt(process.argv[2]);

    for (let counter = 0; counter < number; counter++) {
        console.log(myVar);
    }
}
else if (process.argv.length == 2) {
    console.log("Missing number of occurrences")
}
