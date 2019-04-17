
//js reverse string
function reverseString(str) {
 n = ""
 for(i = 0; i <=str.length; i++) {
   n = str[i] + n
 }
 return n;
}

function reverseStringWithArrays(str) {
  // str.split('') could also be replaced with Array.from(str)
  return str.split('').reverse().join('')
}

// Array.prototype.entries()
a = ["winnie", "parviz"]
b = a.entries()
b.next()
// >> { value: [0, 'winnie'], done: false }
a.push('foo')
b.next().value
// >> [1, 'parviz']
b.next().value
// >> [2, 'foo']
b.next()
// >> { value: undefined, done: true }

// numbers, strings, booleans ARE IMMUTABLE and are not objects
// objects are mutable

// arr.slice() and [...arr] both return copies of arr therefore
// comparisons will be false unless a new var is set to the original array
arr = [0, 1, 2, 4, 5];
arr2 = arr
arr == arr2
// >> true
arr3 = [...arr]
arr == arr3
// >> false
arr4 = arr.slice()
arr == arr4
// >> false

// js for loops
// arr = [0, 1, 2, 3]
for (let i = 0; i < arr.length; i++) {
  // do something with arr[i]
}

for (i in arr) {
  // do something with arr[i] or the index of another array
}

for (let foo of arr) {
  // do something with foo, which is the value of arr at the current loop index
}

// a note on reduce: [].reduce((collector, itemInArray, index) => {}, []
// you can omit the index and do something more simple like the following
// [].reduce((a,b) => a + b)

// [].some(item => <expression goes here>) true means at least one element passes
// [].every(item => <expression>) true means all elements pass
// writing own every function twice
function every(array, test) {
  passes = true;
  array.forEach(item => {
    const pass = test(item);
    if (!pass) {
      passes = false;
    }
  })
  return passes;
}
// De Morgan’s laws --> a && b === !(!a || !b)
function every(array, test) {
  return !array.some(item => !test(item));
}

//
function deepObjectComparison(obj1, obj2) {
  let same = true;
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);
  if (keys1.length !== keys2.length) {
      same = false;
  } else {
    for(i in keys1) {
      if ( keys1[i] == keys2[i] && obj1[keys1[i]] == obj2[keys1[i]]) {
        continue;
      } else {
        same = false;
        break;
      }
    }
  }
  return same;
}

//******* STUDY ME!!! *********
// ---This commented out one was the one I wrote first, then googled
function deepEqual(val1, val2, i=0) {
  if (typeof val1 === 'object' && typeof val2 === 'object') {
    keys = Object.keys(val1);
    keys2 = Object.keys(val2);

    if (keys[i] === keys2[i]) {
      one = val1[keys[i]];
      two = val2[keys2[i]];

      if (one === two) {
        return true;
      } else if (typeof one === "object" && typeof two === "object") {

        if ( deepEqual(one, two, 0) ) {
          return deepEqual(val1, val2, i+1);
        }

      } else return false;
    } else return false;
  } else if (val1 === val2) {
    return true;
  } else return false;
}

function deepEqual(obj1, obj2) {
  if (obj1 === obj2) {
    return true;
  } else if (
    (typeof obj1 == "object" && obj1 != null)
    && (typeof obj2 == "object" && obj2 != null)
  ) {

    if (Object.keys(obj1).length != Object.keys(obj2).length) {
      return false;
    }

    for (var property in obj1) {
      // *** remember for in and hasOwnProperty
      if (obj2.hasOwnProperty(prop)) {

        if (!deepEqual(obj1[prop], obj2[prop])) {
          return false;
        }
      } else return false;
    }

    return true;
  } else return false;
}

function binaryRepresentation(num) {
  n = Math.abs(num)
  // intent was to figure out how to write this func and use
  // Math.clz32(n) to add the zeros to the front
}

function range(start, end, step=1) {
  const arr = [start]

    for(let n = start + step; n != end + step; n = n + step) {
      arr.push( n )
    }

  return arr;
}

function sum(arr) {
	sum = 0
	arr.forEach(item => sum += item)

	return sum;
}
// OR
// function sum(arr) {
// 	return arr.reduce((sum=0, num) => {
//     sum += num
// 	  return sum;
//   })
// }

function reverseArray(arr) {
  const new_arr = []
  arr.forEach(item => new_arr.unshift(item))

  return new_arr;
}

//******* STUDY ME!!! ********
function reverseArrayInPlace(arr) {
	const half = Math.floor(arr.length / 2); // to increase efficiency, remove the half variable, but lose readability
  for (let i = 0; i < half; i++) {
	  toSwap = arr[ arr.length - (i + 1) ]
    arr[arr.length - (i + 1)] = arr[i]
    arr[i] = toSwap
  }
  return arr;
}

//******* STUDY ME!!! *******
function arrayToLinkedList(arr) {
  // iterate backwards through the array to build up the linked list
  list = {}
  for (let i = arr.length - 1; i >= 0; i--) {
    if (i == (arr.length - 1)) {
      list.value = arr[i];
      list.rest = null;
    } else {
      list = { value: arr[i], rest: { ...list } };
    }
  }

  return list;
}

//******* STUDY ME!!! *********
function linkedListToArray(linkedList) {
  arr = []
  const buildArray = (list) => {
    arr.push(list.value);
    if (list.rest) {
      buildArray(list.rest)
    }
  }
  buildArray(linkedList);
  return arr;
}

function AlternativeLinkedListToArray(list, arr = []) {
  arr.push(list.value);
  if (list.rest) {
    return AlternativeLinkedListToArray(list.rest, arr);
  } else return arr;
}

function prepend(item, linkedList) {
  return { value: item, rest: linkedList };
}

// returns element at the given list position or undefined
function nth(linkedList, index) {
  arr = linkedListToArray(linkedList)
  return arr[index];
}

function recursiveNth(linkedList, index, current=0) {
  if (current === index) {
    return linkedList.value;
  } else if (linkedList.rest) {
    return recursiveNth(linkedList.rest, index, current + 1);
  } else return undefined;
}

// *** Remember about emojis and how they take up 2 characters with UTF-16
// UTF-16 describes most common characters using a single 16-bit code unit
// but uses a pair of two such units for others. See below.
//
// Two emoji characters, horse and shoe
let horseShoe = "🐴👟";
console.log(horseShoe.length);
// → 4
console.log(horseShoe[0]);
// → (Invalid half-character)
console.log(horseShoe.charCodeAt(0));
// → 55357 (Code of the half-character)
console.log(horseShoe.codePointAt(0));
// → 128052 (Actual code for horse emoji)
//
// for of loop lets you loop thru actual string characters
let roseDragon = "🌹🐉";
for (let char of roseDragon) {
  console.log(char);
}
// → 🌹
// → 🐉

function loop(value, testFunc, updateFunc, bodyFunc) {
  let passes = true;
  let currentValue = value;

  const testAndUpdate = (val) => {
    passes = testFunc(val);
    if (passes) {
      bodyFunc(val);
      currentValue = updateFunc(val);
    }
  }

  while(passes) {
  	testAndUpdate(currentValue);
  }
}

loop(3, n => n > 0, n => n - 1, console.log);
// → 3
// → 2
// → 1

// ******** STUDY ME ********
// Not understanding how this really works
function debounce(func, delay) {
  let timeout;

  return () => {
    const call = () => {
      timeout = null;
      func.apply(this, arguments);
    };

    clearTimeout(timeout);
    timeout = setTimeout(call, delay);
  };
};

// function debounce(func, delay, now) {
//   let timeout;
//
//   return () => {
//     const call = () => {
//       timeout = null;
//       if (!now) func.apply(this, arguments);
//     };
//
//     if (timeout) clearTimeout(timeout);
//     timeout = setTimeout(call, delay);
//     if (now && !timeout) func.apply(this, arguments)
//   };
// };

var print = debounce(() => console.log('a'), 2000);

print();
print();
print();
print();
print();
print();
print();
print();
print();




/*
    REACT NOTES:

    FLUX                                   VS       REDUX

    Action -> dispatcher -> store -> view   |   immutable state
                                            |
    numerous stores                         |   single store
                                            |
    optional reducers                       |   dispatcher is part of store
                                            |
    separate dispatcher                     |   mandatory reducers
                                            |

    BOTH:
      one way data flow keeping views lightweight,
      separating out action creators enables easier testing of expected functionality,
      stores fuel the views




    basic stateful React MyComponent looks like the following:

    import React from 'react';
    import PropTypes from 'prop-types';

    export default class Component extends React.Component {

    static propTypes = {
      text: PropTypes.string
    }

    constructor() {
      super();
      this.state = {
        foo: 'bar'
      };
    }

    myMethod() {
      // do something
    }

    render() {
      return (
        <div>{ this.props.text }</div>
      );
    }
  }

  can also do:

  MyComponent.propTypes = propTypes;

  and define propTypes outside of component instead of defining as static
  THEN export the component, instead of at the class definition

  export default MyComponent;
*/

























//
