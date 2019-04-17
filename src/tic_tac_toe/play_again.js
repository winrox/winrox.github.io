import React from 'react';

function PlayAgain( props ) {
  return (
    <button onClick={ props.playAgainClickHandler } style={{ marginBottom: "15px" }}>
      Play Again
    </button>
  );
}

export default PlayAgain;
