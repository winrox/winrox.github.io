import React from 'react';
import Spinner from './spinner';

const AWS = require('aws-sdk');
const awsDyDBParams = {
  region: 'us-east-2',
  accessKeyId: process.env.REACT_APP_YOUR_MOM,
  secretAccessKey: process.env.REACT_APP_F_U,
  dynamodb: '2012-08-10'
};

const pickANumber = ( min, max ) => Math.round( Math.random() * ( max - min ) + min );

class Snake extends React.Component {

  constructor() {
    super();
    this.newGameState = {
      snakeList:   null,
      foodList:    null,
      lastFood:    null,
      direction:   null,
      eaten:       null,
      score:       null,
      running:     false,
      rainbow:     null,
      death:       null,
      interval:    20
    };
    this.state = {
      ...this.newGameState,
      cWidth: 500,
      cHeight: 500,
      snakeSegment: {
        width: 20,
        height: 20,
        color: '#264d00'
      },
      scores: null,
      showHighScoreTrophy: false,
      showTopScoresYay: false
    };
    this.foods = [{
      type: 'original',
      width: 20,
      height: 20,
      color: 'brown',
      value: 1
    },{
      type: 'twice',
      width: 20,
      height: 20,
      color: 'yellow',
      value: 2,
    },{
      type: 'rainbow',
      width: 25,
      height: 25,
      color: () => this.getRainbowGradient( true ),
      value: 5
    },{
      type: 'death',
      width: 50,
      height: 50,
      color: () => this.getCautionGradient( 50, 50 ),
      value: -50,
    }];
    this.ctx = null;
  }

  componentDidMount() {
    const canvas = document.getElementById('canvas');
    this.ctx = canvas.getContext('2d');
    this.ctx.font = "25px Arial";
    this.ctx.fillStyle = "#fff";
    this.ctx.fillText( "Click me or press Enter to start the game", 20, 250 );
    canvas.onmousedown = this.canvasMouseDown.bind(this);

    this.drawFoodKey();

    window.addEventListener("keydown", this.onKeyPress.bind(this));
    this.fetchHighScores();
  }

  componentWillUnmount() {
    window.removeEventListener("keydown", this.onKeyPress.bind(this));
  }

  drawFoodKey() {
    const foodKey = document.getElementById('foodKey');
    const keyCtx = foodKey.getContext('2d');
    keyCtx.fillStyle = "#fff";

    keyCtx.save();

    const original = this.foods[0];
    keyCtx.fillStyle = original.color;
    keyCtx.fillRect( 25, 25, original.width, original.height );
    keyCtx.fillStyle = 'black';
    keyCtx.fillText( `${original.value} pt`, 25, 60);
    keyCtx.beginPath();
    keyCtx.moveTo(0, 70);
    keyCtx.lineTo(75, 70);
    keyCtx.stroke();

    const twice = this.foods[1];
    keyCtx.fillStyle = twice.color;
    keyCtx.fillRect( 25, 85, twice.width, twice.height );
    keyCtx.fillStyle = 'black';
    keyCtx.fillText( `${twice.value} pts`, 25, 120);
    keyCtx.beginPath();
    keyCtx.moveTo(0, 130);
    keyCtx.lineTo(75, 130);
    keyCtx.stroke();

    const rainbow = this.foods[2];
    keyCtx.fillStyle = this.getRainbowGradient(true, { ctx: keyCtx, position: { x: 25, y: 150, i: 2 } });
    keyCtx.fillRect( 25, 150, rainbow.width, rainbow.height );
    keyCtx.fillStyle = 'black';
    keyCtx.fillText( `${rainbow.value} pts`, 25, 190);
    keyCtx.fillText( 'speeds up play', 5, 210);
    keyCtx.fillText( 'for a while', 15, 220);
    keyCtx.beginPath();
    keyCtx.moveTo(0, 230);
    keyCtx.lineTo(75, 230);
    keyCtx.stroke();

    const danger = this.foods[3];
    keyCtx.fillStyle = this.getCautionGradient(50, 50, { ctx: keyCtx, position: { x: 12, y: 240, i: 3 } });
    keyCtx.fillRect( 12, 240, danger.width, danger.height );
    keyCtx.fillStyle = 'black';
    keyCtx.fillText( `${danger.value} pts`, 20, 310);
    keyCtx.fillText( 'AVOID ME!', 15, 330);
    keyCtx.fillText( 'disappears', 15, 340);
    keyCtx.fillText( 'when not eaten.', 5, 350);

    keyCtx.restore();
  }

  fetchHighScores = async () => {
    const DynamoDB = await new AWS.DynamoDB( awsDyDBParams );
    const highScores = await DynamoDB.scan({
      TableName: "Snake",
      AttributesToGet: [ "scores" ]
    }).promise(); // => data.Items[0] = { scores: { S: <string value> } }
    const scores = highScores.Items.reduce( ( scores, item, i ) => {
      const row = item.scores['S'];
      const initials = row.slice(0, 3);
      const value = parseInt( row.slice(4) );
      const prevVal = scores.length > 0
        ? scores[ i - 1 ].score
        : 0;
      const findIndexAndPush = ( i ) => {
        const nextPrevVal = i > 1
          ? scores[ i - 2 ].score
          : null;
        if ( !nextPrevVal || value < nextPrevVal ) {
          scores.splice( i - 1, 0, { score: value, initials } );
        } else findIndexAndPush( i - 1 )
      }

      if ( value <= prevVal || i === 0 ) {
        scores.push( { score: value, initials } );
      } else findIndexAndPush( i );

      return scores;
    }, [] );
    this.setState({ scores });
  }

  canvasMouseDown = () => {
    const running = this.state.running;
    if ( !running ) this.startGame();
  }

  onKeyPress = ( event ) => {
    event.preventDefault();
    const { keyCode } = event;
    const { running, direction: direct } = this.state;
    let direction = direct;
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
    } else if ( keyCode === 13 /*Enter*/ && !running ) {
      this.startGame();
    } else if ( keyCode === 27 && running ) {
      this.setState({ running: false });
      this.ctx.fillText( 'Game Reset. Click or hit Enter to play.', 40, 250 );
    }

    if ( direction !== this.state.direction ) {
      this.setState({ direction });
    }
    return;
  }

  foodCollision = ( snake, food ) => {
    const { foods, state: { snakeSegment } } = this;
    return (
      ( snake.x <= food.x + foods[ food.i ].width ) &&
      ( food.x <= snake.x + snakeSegment.width ) &&
      ( snake.y <= food.y + foods[ food.i ].height ) &&
      ( food.y <= snake.y + snakeSegment.height )
    );
  }

  snakeCollision = ( snake1, snake2 ) => (
    ( Math.abs( snake1.x - snake2.x ) < 3 ) &&
    ( Math.abs( snake1.y - snake2.y ) < 3 )
  )

  getSkin = async ( type = 'original' ) => {
    let skin;
    if ( type === 'rainbow' || this.state.interval === 14 ) skin = this.getRainbowGradient( 0, 0, 500, 0 );
    else {
      const snakeSkin = new Image();
      snakeSkin.src = '';
      const snakeSkinPattern = await this.ctx.createPattern( snakeSkin, 'repeat' );
      skin = snakeSkinPattern;
    }

    return skin;
  }

  getRainbowGradient = ( food = false, context ) => {
    let ctx = (context || {}).ctx || this.ctx;
    const f = this.state.foodList && this.state.foodList.length > 0
      ? this.state.foodList[0]
      : context.position;
    const grd = food
      ? ctx.createLinearGradient( f.x, f.y, f.x + 25, f.y + 25 )
      : ctx.createLinearGradient( 0, 0, this.state.cWidth, 0 );
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

  getCautionGradient = ( width, height, context ) => {
    let ctx = (context || {}).ctx || this.ctx;
    const f = this.state.foodList && this.state.foodList.length > 0
      ? this.state.foodList[0]
      : context.position;
    const grd = ctx.createLinearGradient( f.x, f.y, f.x + width, f.y + height );
    grd.addColorStop( 0.1, "orange" );
    grd.addColorStop( 0.2, "red" );
    grd.addColorStop( 0.3, "orange" );
    grd.addColorStop( 0.4, "black" );
    grd.addColorStop( 0.5, "orange" );
    grd.addColorStop( 0.6, "red" );
    grd.addColorStop( 0.7, "orange" );
    grd.addColorStop( 0.8, "black" );
    grd.addColorStop( 0.9, "orange" );
    grd.addColorStop( 1, "red" );
    return grd;
  }

  drawSnake = async ( body, i ) => {
    const { lastFood, snakeSegment } = this.state;
    this.ctx.save();
    if ( i === 0 ) {
      this.ctx.fillStyle = '#000';
    } else this.ctx.fillStyle = await this.getSkin( (lastFood || {}).type || null ) || snakeSegment.color;

    this.ctx.fillRect( body.x, body.y, snakeSegment.width, snakeSegment.height );
    this.ctx.restore();
  }

  drawFood = ( item ) => {
    this.ctx.save();
    const food = this.foods[ item.i ];
    this.ctx.fillStyle = typeof food.color === 'function' ? food.color() : food.color;
    this.ctx.fillRect( item.x, item.y, food.width, food.height );
    this.ctx.restore();
  }

  updateSnakeList = () => {
    const { snakeList, direction, running } = this.state;
    if ( running ) {
      for ( let index = snakeList.length - 1; index >= 0; index-- ) {
        const code = `${ index }${ direction }`;
        const { x, y } = snakeList[ index ];
        if      ( code === '00' ) snakeList[ index ] = { x: snakeList[0].x - 5, y };
        else if ( code === '01' ) snakeList[ index ] = { x, y: snakeList[0].y - 5 };
        else if ( code === '02' ) snakeList[ index ] = { x: snakeList[0].x + 5, y };
        else if ( code === '03' ) snakeList[ index ] = { x, y: snakeList[0].y + 5 };
        else snakeList[ index ] = { x: snakeList[ index - 1 ].x, y: snakeList[ index - 1 ].y };
      };
    }
  }

  handleOffScreenPositioning = () => {
    const { snakeList, running } = this.state;
    if ( running ) {
      let newSnakeList = [ ...snakeList ];

      if ( snakeList[0].x > 498 ) newSnakeList[0].x = 0;
      if ( snakeList[0].x < 0 )   newSnakeList[0].x = 500;
      if ( snakeList[0].y > 498 ) newSnakeList[0].y = 0;
      if ( snakeList[0].y < 0 )   newSnakeList[0].y = 500;

      this.setState({ snakeList: newSnakeList });
    }
  }

  checkForHighScore = async () => {
    await this.fetchHighScores();
    const { score, scores } = this.state;
    const lowestHighScore = scores[ scores.length - 1 ];
    if ( score > lowestHighScore.score || scores.length < 5 ) {
      const DynamoDB = await new AWS.DynamoDB( awsDyDBParams );
      // show congrats message to the user
      if ( score > scores[0].score ) {
        this.setState({ showHighScoreTrophy: true });
      } else this.setState({ showTopScoresYay: true });
      // gather initials info from user
      const initials = prompt( "CONGRATS!!! 🎉 🥳 \nYour score has qualified for the high scores list. \nPlease input your initials below.", "AAA" );
      if ( scores.length <= 5 && initials ) {
        if ( scores.length === 5 ) {
          // remove old item from DB
          await DynamoDB.deleteItem({
            TableName: "Snake",
            Key: { "scores": { S: `${ lowestHighScore.initials } ${lowestHighScore.score}` } }
          }).promise();
        }
        // insert new DB entry
        await DynamoDB.putItem({
          TableName: "Snake",
          Item: { "scores": { S: `${ initials } ${ score }` } }
        }).promise();
        this.fetchHighScores();
      }
    }
  }

  gameOver = () => {
    this.setState({ running: false }, async () => {
      this.ctx.save();
      this.ctx.fillStyle = 'white';
      this.ctx.fillText( 'Game Over! Click or Enter to restart', 45, 250 );
      this.ctx.restore();
      await this.checkForHighScore();
    });
  }

  isGameOver = async () => {
    const { score, snakeList } = this.state;
    let over = false;
    if ( score < 0 ) {
      over = true;
    }
    for ( var i in snakeList ) {
      if ( i === '0' ) continue;
      if ( this.snakeCollision( snakeList[0], snakeList[i] ) ) {
        over = true;
        break;
      }
    }
    return over;
  }

  updateScore = ( foodEaten ) => foodEaten && foodEaten.value
    ? this.state.score + foodEaten.value
    : this.state.score + 1;

  checkForFoodCollision = ( forceNew = false ) => {
    const {
      direction,
      foodList,
      score,
      snakeList
    } = this.state;
    const collision = snakeList.length > 0 &&
      foodList.length > 0 &&
      this.foodCollision( snakeList[0], foodList[0] );

    if ( collision || forceNew ) {
      const lastFood = foodList[0] && foodList[0].i ? this.foods[ foodList[0].i ] : null;
      this.setState({
        lastFood,
        foodList: [],
        eaten: true,
        score: forceNew ? score : this.updateScore( lastFood )
      });
      let newX = snakeList[0].x,
          newY = snakeList[0].y;
      if      ( direction === 0 ) newX = snakeList[0].x - 20;
      else if ( direction === 1 ) newY = snakeList[0].y - 20;
      else if ( direction === 2 ) newX = snakeList[0].x + 20;
      else if ( direction === 3 ) newY = snakeList[0].y + 20;

      if ( lastFood && lastFood.type === 'rainbow' ) {
        this.setState({ interval: 14 });
        setTimeout( () => this.setState({ interval: 20 }), 20000 );
      }

      const list = [ ...snakeList ];
      list.unshift({ x: newX, y: newY });

      this.setState({ snakeList: list });
    }
  }

  generateFood = () => {
    const {
      eaten,
      death,
      rainbow,
      score,
      foodList
    } = this.state;

    if ( eaten ) {
      this.setState({ rainbow: rainbow - 1, death: death - 1 });

      const x = Math.random() * 485 + 5;
      const y = Math.random() * 485 + 5;
      let i; // index to use for selecting food type from this.foods
      if ( death > 0 ) {
        i = rainbow < 1 && Math.round( Math.random() ) ? 2 : Math.round( Math.random() + 0.15 ) ? 0 : pickANumber( 0, 1 );
      } else i = 3;

      const newFoodList = [ ...foodList ];
      newFoodList[0] = { x, y, i }
      this.setState({ foodList: newFoodList });

      if ( i === 2 ) this.setState({ rainbow: Math.round( ( Math.random() + 1 ) ) * pickANumber(25, 50) });
      if ( i === 3 ) {
        // generate new death food number
        const deathNums = function(score) {
          switch(score) {
            case score > 30:
              return [ 30, 48 ];
            case score > 70:
              return [ 20, 40 ];
            case score > 100:
              return [ 10, 25 ];
            case score > 140:
              return [ 10, 15 ];
            case score > 170:
              return [ 8, 15 ];
            case score > 210:
              return [ 1, 8 ];
            default:
              return [ 35, 50 ];
          }
        }(score);
        // set new countdown for death food
        this.setState({ death: pickANumber( deathNums[0], deathNums[1] ) });
        // after some time, make the death food go away if not eaten
        setTimeout( // force new food
          () => !this.state.eaten ? this.checkForFoodCollision( true ) : null,
          score > 100 ? ( pickANumber( 8, 12 )* 1000 ) : 5000
        );
      }
      this.setState({ eaten: false }, this.generateFood );

    } else return;
  }

  updateGame = async () => {
    const { state: { running, foodList, snakeList } } = this;
    if ( running ) this.ctx.clearRect( 0, 0, this.state.cWidth, this.state.cHeight );
    if ( running ) this.generateFood();
    if ( running ) foodList.forEach( this.drawFood );
    if ( running ) snakeList.forEach( this.drawSnake );
    if ( running ) this.checkForFoodCollision();
    if ( running ) this.updateScore();
    const gameOver = await this.isGameOver();
    if ( gameOver ) {
      this.gameOver();
    } else {
      if ( running ) this.handleOffScreenPositioning();
      if ( running ) this.updateSnakeList();
      if ( running ) this.runGame();
    }
  }

  runGame = async () => {
    this.setState({ running: true },
      () => setTimeout( this.updateGame, this.state.interval )
    );
  }

  startGame = () => {
    this.setState({
      ...this.newGameState,
      snakeList: [
        { x: 220, y: 200 },
        { x: 200, y: 200 },
        { x: 180, y: 200 }
      ],
      foodList: [],
      direction: 2,
      eaten: true,
      score: 0,
      death: pickANumber( 50, 70 ),
      rainbow: pickANumber( 15, 40 ),
      showHighScoreTrophy: false,
      showTopScoresYay: false
    }, this.runGame );
  }

  render() {
    const {
      scores,
      showTopScoresYay,
      showHighScoreTrophy
    } = this.state;

    return (
      <React.Fragment>
        <h1>Snake</h1>
        <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'center' }}>
          <div id="canvasWrapper" style={{ float: 'left', paddingRight: '0px' }}>
            <canvas
              height="500"
              width="75"
              style={{
                border: "2px solid black",
                borderRight: 'none',
                backgroundColor: "#fff",
                height: "500px"
              }}
              id="foodKey"
            />
          </div>
          <div id="canvasWrapper" style={{ float: 'left', paddingLeft: '0px' }}>
            <canvas
              height="500"
              width="500"
              style={{
                border: "2px solid black",
                backgroundImage: "url(https://upload.wikimedia.org/wikipedia/en/4/42/Fresh_grass%2C_2014.jpg)",
                backgroundColor: "#00cc00",
                height: "500px",
                backgroundPosition: "center",
                backgroundRepeat: "no-repeat",
                backgroundSize: "cover"
              }}
              id="canvas"
            />
          </div>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
          <div id="score" style={{ textAlign: 'left' }}>Score: { this.state.score || 0 }</div>
            { !scores ?
              <Spinner/>
              :
              <table id="high_scores" style={{ width: '100px' }}>
                <caption>High Scores</caption>
                <tbody>
                  { scores.map( ( entry, i ) => (
                    <tr key={`snake_score_${i}`}>
                      <td>{ entry.score }</td>
                      <td>{ entry.initials }</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            }
            { showHighScoreTrophy &&
              <img
                src="https://media.giphy.com/media/l0Ex3vQtX5VX2YtAQ/giphy.gif"
                alt="Congratulations on getting the high score!!!"
                style={{
                  width: '250px',
                  marginTop: '15px'
                }}
              />
            }
            { showTopScoresYay &&
              <img
                src="https://media.giphy.com/media/HBblEmWutaXQY/giphy.gif"
                alt="Congratulations on getting into the top 5 high scores!"
                style={{
                  width: '250px',
                  marginTop: '15px'
                }}
              />
            }
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default Snake;

// TODO: see if the async await will help any of the gameplay functions
/*
// IDEAS:
// SPECIAL FOOD TYPES:
// // - rainbow food makes snake flash colors and move faster ✅
// // - death food that needs to be avoided that only spawns after you've
// //   reached a certain score just to make the game harder. These will have to
// //   be avoided for a certain amt of time then another food will spawn. ✅
// // - hot pepper food could make fire breathing and break down barriers
// // -
// GAME ADDITIONS:
// // - at higher scores introduce barriers?
// // - concept of levels? every 10 foods eaten perhaps
// // - concept of lives? get 3 lives, and therefore 2 whoopsies
// // - esc to reset/exit ✅
// // - enter to begin as well as click ✅
// // - key for food types ✅
// ASTHETICS:
// // - make snake less blocky
// // - body pattern ✅  TODO: think about fixing, broke at some point
// // - pointed tail
// // - rounded or pointy head
// // - add a background ✅
// // -
// IMPROVEMNTS:
// // - move score outside of game screen ✅
// // - db to hold high score value? ✅
// // - you can get totally off screen, fix it
// // - food can spawn right next to your head, should make that not possible
// //   so that a danger food can't spawn and immediately get you for -50 pts.
// // -
// BUGS:
// // - you can sometimes go through the snake body without a game over
*/
