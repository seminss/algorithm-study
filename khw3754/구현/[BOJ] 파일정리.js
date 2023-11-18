const fs = require('fs');
const [n, ...input] = fs.readFileSync('dev/stdin').toString().trim().split('\n');

const count = {};
let exts = [];
input.forEach(file => {
    const [name, ext] = file.split('.');
    if(ext in count) {
        count[ext] += 1;
    } else {
        exts.push(ext);
        count[ext] = 1;
    }
});

exts.sort().forEach(ext => {
    console.log(ext, count[ext]);
})