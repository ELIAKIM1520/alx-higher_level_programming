#!/usr/bin/node


function factorialize(num) {
    if (num < 0) 
        return -1;

    else if (num == 0) 
        return 1;
    else {
        return (num * factorialize(num - 1));
    }
}

if (process.argv[2]) {
    const myVar = parseInt(process.argv[2]);

    console.log(factorialize(myVar));
}
else if (process.argv.length <= 2) {
    console.log("1");
}
