import React from 'react';

function ScoreBoard( props ) {
  return (
    <table style={{ margin: '0 15px' }}>
        <thead>
          <tr>
            <td colSpan="2">Score:</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>X</strong></td>
            <td><strong>O</strong></td>
          </tr>
          <tr>
            <td><p id="x-score">{ props.scoreX }</p></td>
            <td><p id="o-score">{ props.scoreO }</p></td>
          </tr>
        </tbody>
      </table>
  );
}

export default ScoreBoard;
