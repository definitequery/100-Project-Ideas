import { createInterface } from "readline";

function readInput(promptText = '') {
  return new Promise((resolve) => {
    const rl = createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.question(promptText, (input) => {
      rl.close();
      resolve(input);
    });
  });
}

async function selectMode() {
  let response;
  while (true) {
    response = await readInput('Choose conversion mode. Enter C to convert Celsius temperatures or F to convert Fahrenheit temperatures: ');
    if (response.toLowerCase() === 'c' || response.toLowerCase() === 'f') {
      break;
    }
    console.log('Error: Invalid option. Please choose between C or F.');
  }
  return response.toLowerCase();
}

function convertToCelsius(fahrenheit) {
  return (fahrenheit - 32) * 5 / 9;
}

function convertToFahrenheit(celsius) {
  return celsius * 9 / 5 + 32;
}

async function convertTemperature() {
  console.log('\n*****************');
  const mode = await selectMode();
  
  const tempInput = await readInput(`Enter ${mode.toUpperCase()}° temperature to convert: `);
  const temperature = parseFloat(tempInput);
  if (isNaN(temperature)) {
    console.log("Invalid temperature. Please enter a numeric value.");
    return;
  }

  if (mode === 'c') {
    const fahrenheit = convertToFahrenheit(temperature);
    console.log(`${temperature} degrees Celsius = ${fahrenheit.toFixed(1)} degrees Fahrenheit`);
  } else {
    const celsius = convertToCelsius(temperature);
    console.log(`${temperature} degrees Fahrenheit = ${celsius.toFixed(1)} degrees Celsius`);
  }
  console.log('*****************\n');
}

convertTemperature();
