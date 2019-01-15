const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
ctx.font = "25px Arial";
ctx.fillStyle = "#fff";
ctx.fillText( "Click me or press Enter to start the game", 20, 250 );
const cWidth = 500;
const cHeight = 500;

let snakeList,
    foodList,
    direction,
    eaten,
    intervalVar,
    score,
    running = false;

const snakeSkin = new Image();
snakeSkin.src = 'https://www.decodip.com/wp-content/uploads/Film-AP-161.jpg';
const snakeSkinPattern = ctx.createPattern( snakeSkin, 'repeat' );

const snakeSegment = {
  width: 20,
  height: 20,
  color: snakeSkinPattern
};

const foodAttrs = {
  width: 20,
  height: 20,
  color: 'orange'
};

canvas.onmousedown = () => {
  if ( running ) clearInterval( intervalVar );
  startGame();
}

document.onkeydown = ( event ) => {
  const { keyCode } = event
  if ( keyCode === 37 && direction !== 2) {
    direction = 0; // user hit left and the snake is not going right
  }
  else if ( keyCode === 38 && direction !== 3) {
    direction = 1; // user hit up and is not going down
  }
  else if ( keyCode === 39 && direction !== 0) {
    direction = 2; // user hit right and is not going left
  }
  else if ( keyCode === 40 && direction !== 1) {
    direction = 3; // user hit down and is not going up
  } else if ( keyCode === 13 && !running ) {
    startGame();
  } else if ( keyCode === 27 && running ) {
    clearInterval( intervalVar );
    running = false;
    ctx.fillText( 'Game Reset. Click or hit Enter to play.', 40, 250 );
  }
}

const foodCollision = ( snake, food ) => (
  ( snake.x <= food.x + foodAttrs.width ) &&
  ( food.x <= snake.x + snakeSegment.width ) &&
  ( snake.y <= food.y + foodAttrs.height ) &&
  ( food.y <= snake.y + snakeSegment.height )
);

const snakeCollision = ( snake1, snake2 ) => (
  ( Math.abs( snake1.x - snake2.x ) < 5 ) &&
  ( Math.abs( snake1.y - snake2.y ) < 5 )
);

const getSkin = () => {
  const snakeSkin = new Image();
  snakeSkin.src = 'https://www.decodip.com/wp-content/uploads/Film-AP-161.jpg';
  const snakeSkinPattern = ctx.createPattern( snakeSkin, 'repeat' );

  return snakeSkinPattern;
}

const drawSnake = ( body, i ) => {
  ctx.save();
  if ( i === 0 ) ctx.fillStyle = '#000';
  else ctx.fillStyle = getSkin() || snakeSegment.color;
  ctx.fillRect( body.x, body.y, snakeSegment.width, snakeSegment.height );
  ctx.restore();
}

const drawFood = ( item ) => {
  ctx.save();
  ctx.fillStyle = foodAttrs.color;
  ctx.fillRect( item.x, item.y, foodAttrs.width, foodAttrs.height );
  ctx.restore();
}

const updateSnakeList = () => {
  for ( let index = snakeList.length - 1; index >= 0; index-- ) {
    const code = `${ index }${ direction }`;
    const { x, y } = snakeList[ index ];
    if      ( code === '00' ) snakeList[ index ] = { x: snakeList[0].x - 5, y };
    else if ( code === '01' ) snakeList[ index ] = { x, y: snakeList[0].y - 5 };
    else if ( code === '02' ) snakeList[ index ] = { x: snakeList[0].x + 5, y };
    else if ( code === '03' ) snakeList[ index ] = { x, y: snakeList[0].y + 5 };
    else snakeList[ index ] = { x: snakeList[ index - 1 ].x, y: snakeList[ index - 1 ].y };
  };
};

const handleOffScreenPositioning = () => {
  if ( snakeList[0].x > 500 ) snakeList[0].x = 0;
  if ( snakeList[0].x < 0 )   snakeList[0].x = 500;
  if ( snakeList[0].y > 500 ) snakeList[0].y = 0;
  if ( snakeList[0].y < 0 )   snakeList[0].y = 500;
}

const isGameOver = () => {
  for ( i in snakeList ) {
    if ( i === '0' ) continue;
    if ( snakeCollision( snakeList[0], snakeList[i] ) ) {
      clearInterval( intervalVar );
      ctx.fillText( 'Game Over! Click or Enter to restart', 80, 250 );
      break;
    }
  }
}

const generateFood = () => {
  while( eaten ) {
    const x = Math.random() * 485 + 5;
    const y = Math.random() * 485 + 5;
    foodList[0] = { x, y };
    eaten = false;
  }
}

const checkForCollisions = () => {
  if ( foodCollision( snakeList[0], foodList[0] ) ) {
    foodList = [];
    eaten = true;
    score += 1;
    let newX = snakeList[0].x,
        newY = snakeList[0].y;
    if      ( direction == 0 ) newX = snakeList[0].x - 20;
    else if ( direction == 1 ) newY = snakeList[0].y - 20;
    else if ( direction == 2 ) newX = snakeList[0].x + 20;
    else if ( direction == 3 ) newY = snakeList[0].y + 20;

    snakeList.unshift({ x: newX, y: newY });
  }
}

const updateSnakePosition = () => {
  ctx.clearRect( 0, 0, cWidth, cHeight );
  generateFood();
  foodList.forEach( drawFood );
  snakeList.forEach( drawSnake );
  checkForCollisions();
  ctx.fillText( `Score: ${ score }`, 375, 30 );
  isGameOver();
  handleOffScreenPositioning();
  updateSnakeList();
}

const startGame = () => {
  snakeList = [
    { x: 240, y: 200 },
    { x: 200, y: 200 },
    { x: 180, y: 200 }
  ];
  foodList = [];
  direction = 2;
  eaten = true;
  score = 0;
  running = true;
  intervalVar = setInterval( updateSnakePosition, 20 );
}

// TODO: see if the async await will help any of the gameplay functions
/*
// IDEAS:
// SPECIAL FOOD TYPES:
// // - rainbow food makes snake flash colors and move faster for 5-10 seconds
// // - some foods make the snake change color (not on a timer)
// // - death food that needs to be avoided that only spawns after you've
// //   reached a certain score just to make the game harder. These will have to
// //   be avoided for a certain amt of time then another food will spawn.
// // - hot pepper food could make fire breathing and break down barriers
// // -
// GAME ADDITIONS:
// // - at higher scores introduce barriers?
// // - concept of levels? every 10 foods eaten perhaps
// // - concept of lives? get 3 lives, and therefore 2 whoopsies
// // - esc to reset/exit ✅
// // - enter to begin as well as click ✅
// // -
// ASTHETICS:
// // - make snake less blocky
// // - body pattern ✅
// // - pointed tail
// // - rounded or pointy head
// // - add a background ✅
// // -
// IMPROVEMNTS:
// // - move score outside of game screen
// // - db to hold high score value? firebase?
// // -
*/
