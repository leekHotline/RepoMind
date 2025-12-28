console.log('start time!');

let count = 1;

setTimeout(() => {
    console.log('two seconds passed')
},2000);


setInterval(() => {
    console.log('per five seconds once, ctrl+c to stop')
    console.log(`plus once: ${count++}`)
},5000)