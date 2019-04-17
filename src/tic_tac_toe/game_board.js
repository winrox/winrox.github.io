import React from 'react';
import Tile from './tile';

function GameBoard( props ) {

  const getTileById = ( id ) => props.tiles.find( tile => tile.id === id );
  const { tiles } = props;

  return (
    <div style={{ backgroundColor: '#fff', margin: '0 15px' }}>
      <table>
        <tbody>
          <tr>
            <td>
              <Tile
                tile={ getTileById( tiles[0].id ) }
                clickHandler={ props.clickHandler }
              />
            </td>
            <td style={{ borderLeft: "2px solid #fff", borderRight: "2px solid #fff" }}>
              <Tile
                tile={ getTileById( tiles[1].id) }
                clickHandler={ props.clickHandler }
              />
            </td>
            <td>
              <Tile
                tile={ getTileById( tiles[2].id ) }
                clickHandler={ props.clickHandler }
              />
            </td>
          </tr>
          <tr>
            <td style={{ borderBottom: "2px solid #fff", borderTop: "2px solid #fff" }}>
              <Tile
                tile={ getTileById( tiles[3].id ) }
                clickHandler={ props.clickHandler }
              />
            </td>
            <td style={{ border: "2px solid #fff" }}>
              <Tile
                tile={ getTileById(tiles[4].id) }
                clickHandler={ props.clickHandler }
              />
            </td>
            <td style={{ borderBottom: "2px solid #fff", borderTop: "2px solid #fff" }}>
              <Tile
                tile={ getTileById(tiles[5].id) }
                clickHandler={ props.clickHandler }
              />
            </td>
          </tr>
          <tr>
            <td>
              <Tile
                tile={ getTileById(tiles[6].id) }
                clickHandler={ props.clickHandler }
              />
            </td>
            <td style={{ borderLeft: "2px solid #fff", borderRight: "2px solid #fff" }}>
              <Tile
                tile={ getTileById(tiles[7].id) }
                clickHandler={ props.clickHandler }
              />
            </td>
            <td>
              <Tile
                tile={ getTileById(tiles[8].id) }
                clickHandler={ props.clickHandler }
              />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default GameBoard;
