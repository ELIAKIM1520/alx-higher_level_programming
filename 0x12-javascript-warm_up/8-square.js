#!/usr/bin/node



if (process.argv[2]) {
    const number = process.argv[2];

    for (let counter = 0; counter < number; counter++) {
        console.log("X".repeat(number));
    }
}
else if (process.argv.length == 2) {
    console.log("Missing size");
}
