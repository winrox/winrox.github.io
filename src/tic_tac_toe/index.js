import React from 'react';
import GameBoard from './game_board';
import Message from './message';
import PlayAgain from './play_again';
import ScoreBoard from './score';

class TicTacToe extends React.Component {

  constructor() {
    super();
    this.state = {
      winnerFound: false,
      tiles: [
        { id: "a1", src: "blank" },
        { id: "a2", src: "blank" },
        { id: "a3", src: "blank" },
        { id: "b1", src: "blank" },
        { id: "b2", src: "blank" },
        { id: "b3", src: "blank" },
        { id: "c1", src: "blank" },
        { id: "c2", src: "blank" },
        { id: "c3", src: "blank" }
      ],
      scoreX: 0,
      scoreO: 0,
      alertMessage: '',
      clickCounter: 0,
    };
  }

  isEven = ( num ) => {
    if ( num === 0 ){
      return true;
    } else if( num === 1 ) {
      return false;
    } else if( num < 0 ) {
      return this.isEven( num + 2 );
    }
    else {
      return this.isEven( num - 2 );
    }
  }

  tileClickHandler = tile => {
    const { clickCounter } = this.state;

    if ( this.state.winnerFound === true ) {
      return;
    } else {
      var even = this.isEven( clickCounter );

      if ( tile.src !== 'blank' ) {
        this.setState({alertMessage: "I'm sorry. That spot has already been taken."});
      } else if ( even ) {
        tile.src = "X"
        this.setState({ alertMessage: "", clickCounter: clickCounter + 1 });
      } else if ( !even ) {
        tile.src = "O"
        this.setState({ alertMessage: "", clickCounter: clickCounter + 1 });
      } else {
        this.setState({ clickCounter: this.state.clickCounter - 1 });
      }
    }

    this.findWinner();
  }

  getTileById = ( id ) => this.state.tiles.find( item => item.id === id );

  findWinner = () => {

    const win = [
      ['a1','a2','a3'],
      ['b1','b2','b3'],
      ['c1','c2','c3'],
      ['a1','b1','c1'],
      ['a2','b2','c2'],
      ['a3','b3','c3'],
      ['a1','b2','c3'],
      ['a3','b2','c1']
    ];

    const { scoreO, scoreX, winnerFound } = this.state;

    for( var i in win ) {
      var winIndex = win[i];

      if (
        ( this.getTileById( winIndex[0] ).src === "X" )
        && ( this.getTileById( winIndex[1] ).src === "X" )
        && ( this.getTileById( winIndex[2] ).src === "X" )
      ) {
        this.setState({ winnerFound: true, scoreX: scoreX + 1, alertMessage: "X wins!" });
      } else if (
        ( this.getTileById( winIndex[0] ).src === "O" )
        && ( this.getTileById( winIndex[1] ).src === "O" )
        && ( this.getTileById( winIndex[2] ).src === "O" )
      ) {
        this.setState({ winnerFound: true, scoreO: scoreO + 1, alertMessage: "O wins!" });
      }
    }

    if ( this.state.clickCounter === 8 && winnerFound === false ) {
      this.setState({ alertMessage: "No winner this time. Please play again.", winnerFound: true });
    }
  }

  playAgainClickHandler = () => {
    this.clearGame();
    this.setState({ alertMessage: "", winnerFound: false, clickCounter: 0 });
    //hide play again button
  }

  clearGame = () => {
    const tiles = [
      { id: "a1", src: "blank" },
      { id: "a2", src: "blank" },
      { id: "a3", src: "blank" },
      { id: "b1", src: "blank" },
      { id: "b2", src: "blank" },
      { id: "b3", src: "blank" },
      { id: "c1", src: "blank" },
      { id: "c2", src: "blank" },
      { id: "c3", src: "blank" }
    ];

    this.setState({ tiles: tiles });
  }

  render() {
    const { tiles, scoreX, scoreO, winnerFound, clickCounter, alertMessage } = this.state;

    return (
      <React.Fragment>
        <h1>
          Tic Tac Toe
        </h1>
        <p style={{ padding: '0 30px' }}>This was a project that I orginally wrote in 2015 when I first started learning JS. I re-wrote it in react shortly after, and It has been tweaked from that slightly for implementation on this site, but the original code can be found <a href="https://github.com/winrox/tic_tac_toe">here</a> and in React <a href="https://github.com/winrox/react_tic_tac_toe">here</a>.</p>
        <div style={{ display: 'inline-flex' }}>
          <GameBoard
            tiles        = { tiles }
            winnerFound  = { winnerFound }
            clickCounter = { clickCounter }
            alertMessage = { alertMessage }
            clickHandler = { this.tileClickHandler }
          />
          <div style={{ display: 'flex', flexDirection: 'column', width: '100px' }}>
            <ScoreBoard  scoreX={ scoreX } scoreO={ scoreO } />
            <Message  alertMessage={ alertMessage } winnerFound={ winnerFound } />
            { winnerFound &&
              <PlayAgain  playAgainClickHandler={ this.playAgainClickHandler } />
            }
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default TicTacToe;
