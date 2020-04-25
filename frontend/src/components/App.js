import React, { useState, useEffect } from 'react';
import logo  from '../assets/logo.png';
import Blockchain from './Blockchain'

// useState reads what the data is being typed over a singlt stable state
import { API_BASE_URL } from '../config'

function App() {
  const [walletInfo, setWalletInfo ] = useState({})

  useEffect( () => {
    fetch(`${API_BASE_URL}/wallet/info`)
    .then(response => response.json())
    .then(json => setWalletInfo(json));
  }, []);
  
  const { address, balance } = walletInfo;

  return (
    <div className="App">
      <img className="logo" src={logo} alt= "application-logo" />
      <h1>Welcome to blockchain</h1>
      <br />
      <div className="WalletInfo">
        <div>Address: {address}</div>
        
      </div>
      <br />
      <Blockchain /> 
    </div>
  );
}

export default App;
//<div>Balance: {balance}</div>