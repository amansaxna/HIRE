//import React, { useState } from 'react';
//import Joke from './Joke';
// useState reads what the data is being typed over a singlt stable state

//function App() {
//  const [userQuery, setUserQuery] = useState('');
////
////  const updateUserQuery = event => {
//    console.log('userQuery', userQuery);
//
//    setUserQuery(event.target.value);
//  }
//
//  const searchQuery = () => {
//    window.open(`https://google.com/search?q=${userQuery}`);
//  }
//
//  const handelKeyPress = (event) => {
//    if(event.key === 'Enter')
//      searchQuery();
//  }
//
//  return (
//    <div className="App">
//      <input value={userQuery} onChange={updateUserQuery} />
//      <button onClick={searchQuery} onKeyPress={handelKeyPress}>Search</button>
//      <hr/>
//      <Joke />
//    </div>
//  );
//}
//
//export default App;
