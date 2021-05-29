var os = require("os")

hostname = os.hostname();
totalmem = os.totalmem();
freemem = os.freemem();
cpus = os.cpus();

console.log(`host name : ${hostname}`);
console.log(`total memory : ${totalmem}`);
console.log(`free memory : ${freemem}`);
console.log('CPU info :\n');
console.dir(cpus)