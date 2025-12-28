import {randomBytes} from 'crypto';


const randString = randomBytes(16).toString('hex');

console.log(`Random string is: ${randString}`);