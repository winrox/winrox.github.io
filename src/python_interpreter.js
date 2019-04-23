const { whatToExecute } = require('./instructions');

class PythonInterpreter {

  constructor() {
    this.stack = [];
  }

  loadValue(number) {
    this.stack.push(number);
    this.environment = {};
  }

  storeName(name) {
    const value = this.stack.pop();
    this.environment[name] = value;
  }

  loadName(name) {
    const value = this.environment[name];
    this.stack.push(value);
  }

  parseAgrument(instruction, argument, whatToExecute) {
    // Understand what the argument to each instruction means
    const numbers = ["LOAD_VALUE"]
    const names = ["LOAD_NAME", "STORE_NAME"]
    let arg = argument;

    if (instruction in numbers) {
      arg = what_to_execute["numbers"][argument]
    } else if (instruction in names) {
      arg = what_to_execute["names"][argument]
    }

    return arg;
  }

  printAnswer() {
    const answer = this.stack.pop();
    console.log(answer);
  }

  addTwoValues() {
    const firstNum = this.stack.pop();
    const secondNum = this.stack.pop();
    const total = firstNum + secondNum;
    this.stack.push(total);
  }

  runCode(whatToExecute) {
    const code = JSON.parse(whatToExecute);
    const instructions = code.instructions;
    for (const step of instructions) {
      const [ instruction, argument ] = step;
      const arg = this.parse_argument(instruction, argument, what_to_execute);

      if (instruction === 'LOAD_VALUE') {
        const num = code.numbers[arg];
        this.loadValue(num);
      } else if (instruction === 'ADD_TWO_VALUES') {
        this.addTwoValues();
      } else if (instruction === 'PRINT_ANSWER' ) {
        this.printAnswer();
      } else if (instruction === 'STORE_NAME') {
        this.storeName(arg);
      } else if (instruction === 'LOAD_NAME') {
        this.loadName(arg);
      }
    }
  }
}

const interpreter = new PythonInterpreter();
interpreter.runCode(whatToExecute);
