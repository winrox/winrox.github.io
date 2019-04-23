const { whatToExecute } = require('./instructions');

// understand these 3 instructions for now.
//
// LOAD_VALUE
// ADD_TWO_VALUES
// PRINT_ANSWER
//
// 7 + 5
//
// will need to make sure that None is changed to null and tuples are converted to arrays
// const whatToExecute = {
//     "instructions": [
//       ("LOAD_VALUE", 0),
//       ("LOAD_VALUE", 1),
//       ("ADD_TWO_VALUES", None),
//       ("PRINT_ANSWER", None)
//     ],
//     "numbers": [7, 5]
//   };

class PythonInterpreter {

  constructor() {
    this.stack = [];
  }

  loadValue(number) {
    this.stack.push(number);
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
    for (const [instruction, argument] of instructions) {
      if (instruction === 'LOAD_VALUE') {
        const num = code.numbers[argument];
        this.loadValue(num);
      } else if (instruction === 'ADD_TWO_VALUES') {
        this.addTwoValues();
      } else if ( instruction === 'PRINT_ANSWER' ) {
        this.printAnswer();
      }
    }
  }
}

const interpreter = new PythonInterpreter();
interpreter.runCode(whatToExecute);
