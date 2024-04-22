#!/usr/bin/node

argvCount = 0;

for (argvCount in process.argv) {
    argvCount++;
}

if (argvCount <= 2) {
    console.log('No argument');
}
else if (argvCount === 3) {
    let arg = process.argv[2];
    console.log(arg);
}

