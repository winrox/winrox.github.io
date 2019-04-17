import React from 'react';

function Spinner () {
  return (
    <img src="https://media2.giphy.com/media/fBGoErRAVldV0VVJdg/200w.webp?cid=3640f6095c6f06de4150344e731d737d" alt="loading spinner" />
  );
}

export default Spinner;

// import React       from 'react';
// import css         from './Spinner.css';
// import LoadingIcon from '../../resources/icons/svg/loading.svg';
// import classNames  from 'classnames';
//
// export default function Spinner( props ) {
//   const classes = classNames({
//     [ css.loading ] : true,
//     [ props.className ] : props.className
//   });
//
//   return (
//     <div className={ classes } style={ props.style }>
//       <LoadingIcon className={ css.spinner } style={ props.iconStyle } />
//       { props.text &&
//         <span className={ css.text }>{ props.text }</span>
//       }
//     </div>
//   );
// }
