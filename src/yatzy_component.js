import React from 'react';

class PythonYatzyShell extends React.Component {

  constructor() {
    super();
    this.pyshell = null;
  }

  componentDidMount() {
  }

  myMethod () {}

  render() {

    return (
      <div>
        <h1>Python Yatzy</h1>
        <iframe
          src="https://trinket.io/embed/python3/1ca564d860?outputOnly=true&runOption=run&start=result"
          height="700"
          frameBorder="0"
          marginHeight="0"
          allowFullScreen
          title="trinket.io hosted Python Yatzy by Winnie Palangpour"
          style={{ minWidth: '570px', width: 'auto', margin: '0 15px' }}
        ></iframe>
      </div>
    );
  }
}

export default PythonYatzyShell;
