import React from 'react';

function AlertMessage( props ) {
  return (
    <div style={{
      textAlign: 'center',
      fontSize: 'large',
      fontWeight: 'bold'
    }}>
      { props.alertMessage }
    </div>
  );
}

export default AlertMessage;
