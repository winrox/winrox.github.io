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
      <div style={{ width: '50%', marginLeft: '25%' }}>
        <h1>Python Yatzy</h1>
        <iframe
          src="https://trinket.io/embed/python3/264ce0a0f4?outputOnly=true&runOption=run&start=result"
          width="100%"
          height="700"
          frameBorder="0"
          marginWidth="0"
          marginHeight="0"
          allowFullScreen
          title="trinket.io hosted Python Yatzy by Winnie Palangpour"
        ></iframe>
      </div>
    );
  }
}

export default PythonYatzyShell;
