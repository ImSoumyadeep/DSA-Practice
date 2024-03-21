// index.js

//  import the crypto module
const crypto = require("crypto");



//  get a commands using process.argv
const operation = process.argv[2];


// complete the  function

switch (operation) {
  case 'add':
    console.log(parseInt(process.argv[3])+parseInt(process.argv[4]));
    break;
  case 'sub':
    console.log(process.argv[3]-process.argv[4]);
    break;
  case 'mult':
    console.log(process.argv[3]*process.argv[4]);
    break;
  case 'divide':
    console.log(process.argv[3]/process.argv[4]);
    break;
  case 'sin':
    console.log(Math.sin(process.argv[3]));
    break;
  case 'cos':
    console.log(Math.cos(process.argv[3]));
    break;
  case 'tan':
    console.log(Math.tan(process.argv[3]));
    break;
  case 'random':
    (process.argv.length === 4) ? 
      console.log(crypto.randomBytes(process.argv[3]/2).toString('hex')): 
        console.log("Provide length for random number generation.");
    break;
  default:
    console.log("Invalid operation");
}
