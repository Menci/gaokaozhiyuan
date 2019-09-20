const data = require('fs').readFileSync(process.argv[2]).toString().trim().split('\n').map(l => l.trim().split('\t').map(x => parseInt(x))).filter(l => l.length == 2);
let cnt = 0, sum = 0;
for (const item of data) sum += item[0] * item[1], cnt += item[1];
let avg = sum / cnt, ss = 0;
for (const item of data) ss += Math.pow(item[0] - avg, 2) * item[1];
console.log({ cnt, sum, avg, std: Math.sqrt(ss / cnt) })
