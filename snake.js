const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
ctx.font = "25px Arial";
ctx.fillStyle = "#fff";
ctx.fillText( "Click me or press Enter to start the game", 20, 250 );
const cWidth = 500;
const cHeight = 500;
const pickANumber = ( min, max ) => Math.round( Math.random() * ( max - min ) + min );

let snakeList,
    foodList,
    nextFood,
    lastFood,
    direction,
    eaten,
    intervalVar,
    score,
    running = false,
    rainbow = pickANumber( 15, 40 ),
    interval = 20;

const snakeSegment = {
  width: 20,
  height: 20,
  color: '#264d00'
};

const getRainbowGradient = ( food = false ) => {
  const f = foodList[0];
  const grd = food
    ? ctx.createLinearGradient( f.x, f.y, f.x + 25, f.y + 25 )
    : ctx.createLinearGradient( 0, 0, cWidth, 0 );
  grd.addColorStop( 0.1, "red" );
  grd.addColorStop( 0.2, "orange" );
  grd.addColorStop( 0.3, "yellow" );
  grd.addColorStop( 0.4, "green" );
  grd.addColorStop( 0.5, "#006666" );
  grd.addColorStop( 0.6, "blue" );
  grd.addColorStop( 0.7, "indigo" );
  grd.addColorStop( 0.8, "purple" );
  grd.addColorStop( 0.9, "#ff0066" );
  grd.addColorStop( 1, "red" );

  return grd;
}

const foods = [{
  type: 'original',
  width: 20,
  height: 20,
  color: () => '#ffcc00',
  value: 1
},{
  type: 'rainbow',
  width: 25,
  height: 25,
  color: () => getRainbowGradient( true ),
  value: 5
}];

canvas.onmousedown = () => {
  if ( !running ) startGame();
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
    running = false;
    ctx.fillText( 'Game Reset. Click or hit Enter to play.', 40, 250 );
  }
}

const foodCollision = ( snake, food ) => (
  ( snake.x <= food.x + foods[ food.i ].width ) &&
  ( food.x <= snake.x + snakeSegment.width ) &&
  ( snake.y <= food.y + foods[ food.i ].height ) &&
  ( food.y <= snake.y + snakeSegment.height )
);

const snakeCollision = ( snake1, snake2 ) => (
  ( Math.abs( snake1.x - snake2.x ) < 5 ) &&
  ( Math.abs( snake1.y - snake2.y ) < 5 )
);

const getSkin = ( type = 'original' ) => {
  let skin;
  if ( type === 'rainbow' || interval === 14 ) skin = getRainbowGradient( 0, 0, 500, 0 );
  else {
    const snakeSkin = new Image();
    snakeSkin.src = 'https://www.decodip.com/wp-content/uploads/Film-AP-161.jpg';
    const snakeSkinPattern = ctx.createPattern( snakeSkin, 'repeat' );
    skin = snakeSkinPattern;
  }

  return skin;
}

const drawSnake = ( body, i ) => {
  ctx.save();
  if ( i === 0 ) {
    ctx.fillStyle = '#000';
  } else ctx.fillStyle = getSkin( (lastFood || {}).type || null ) || snakeSegment.color;

  ctx.fillRect( body.x, body.y, snakeSegment.width, snakeSegment.height );
  ctx.restore();
}

const drawFood = ( item ) => {
  ctx.save();
  const food = foods[ item.i ];
  ctx.fillStyle = food.color();
  ctx.fillRect( item.x, item.y, food.width, food.height );
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
      running = false;
      ctx.fillText( 'Game Over! Click or Enter to restart', 45, 250 );
      break;
    }
  }
}

const generateFood = () => {
  while( eaten ) {
    rainbow--;
    const x = Math.random() * 485 + 5;
    const y = Math.random() * 485 + 5;
    const i = rainbow < 1 && Math.round( Math.random() ) ? 1 : 0;
    if ( i === 1 ) rainbow = Math.round( ( Math.random() + 1 ) ) * pickANumber(25, 50);
    nextFood = { x, y, i };
    foodList[0] = nextFood;
    eaten = false;
  }
}

const checkForFoodCollision = () => {
  if ( foodCollision( snakeList[0], foodList[0] ) ) {
    lastFood = foodList[0] && foodList[0].i ? foods[ foodList[0].i ] : null;
    foodList = [];
    eaten = true;
    score = lastFood && lastFood.value ? score + lastFood.value : score + 1;
    let newX = snakeList[0].x,
        newY = snakeList[0].y;
    if      ( direction == 0 ) newX = snakeList[0].x - 20;
    else if ( direction == 1 ) newY = snakeList[0].y - 20;
    else if ( direction == 2 ) newX = snakeList[0].x + 20;
    else if ( direction == 3 ) newY = snakeList[0].y + 20;

    if ( lastFood && lastFood.type === 'rainbow' ) {
      interval = 14;
      setTimeout( () => interval = 20, 20000 );
    }
    snakeList.unshift({ x: newX, y: newY });
  }
}

const updateSnakePosition = () => {
  ctx.clearRect( 0, 0, cWidth, cHeight );
  generateFood();
  foodList.forEach( drawFood );
  snakeList.forEach( drawSnake );
  checkForFoodCollision();
  ctx.fillText( `Score: ${ score }`, 375, 30 );
  isGameOver();
  handleOffScreenPositioning();
  updateSnakeList();
  if ( running ) runGame();
}

const runGame = () => {
  setTimeout( updateSnakePosition, interval );
}

const stopGame = () => {

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
  runGame();
}

// TODO: see if the async await will help any of the gameplay functions
/*
// IDEAS:
// SPECIAL FOOD TYPES:
// // - rainbow food makes snake flash colors and move faster ✅
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
// // - you can get totally off screen, fix it
// // -
*/
