import { createInterface } from 'node:readline';

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

function greetName(name) {
  let response;
  response = `Hello, ${name}`;
  return response;
}

rl.question('What is your name? : ', name => {
  console.log(greetName(name));
  rl.close();
});
