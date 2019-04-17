import React from 'react';
import './App.css';
import TicTacToe from './tic_tac_toe';
import Snake from './snake';
import PythonYatzyShell from './yatzy_component';

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <div className="intro">
          <h1>Winnie's Games</h1>
          <div className="whoKnows">
            <p>Hey there! Feel like playing snake, yatzy, or tic tac toe? You do!? Great, check it out!</p>
          </div>
        </div>
        <div className="snake">
          <Snake />
        </div>
        <div className="yatzy">
          <PythonYatzyShell />
        </div>
        <div className="tictactoe">
          <TicTacToe />
        </div>
      </div>
    );
  }
}

export default App;
