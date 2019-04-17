import React from 'react';

function Tile( props ) {
  const source = props.tile.src === 'X'
    ? 'https://raw.githubusercontent.com/winrox/react_tic_tac_toe/master/img/X.png'
    : props.tile.src === 'O'
      ? 'https://raw.githubusercontent.com/winrox/react_tic_tac_toe/master/img/O.png'
      : 'https://raw.githubusercontent.com/winrox/react_tic_tac_toe/master/img/blank.png';

  return (
    <img
      id={ props.tile.id }
      src={ source }
      onClick={ () => props.clickHandler( props.tile ) }
      alt="game tile"
      width="100px"
      height="100px"
    />
  );
}

export default Tile;
