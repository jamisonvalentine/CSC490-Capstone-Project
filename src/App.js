<<<<<<< HEAD
import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  function showInput() {
    alert("you clicked a button");
  }

  return (
    <div className="App">
      <h3>Select a class</h3>
      <h3>View the school's with an equivalent course</h3>
      <input id="search" type="text"></input>
      <button onClick={showInput}>Submit</button>
=======
import React from 'react';
import Home from './components/Home';
import {
  Switch,
  Route,
  match
} from "react-router-dom";
import About from './components/About';
import Error from './components/404';
import Search from './components/Search';

function App() {
  return (
    <div className='app d-flex flex-column justify-content-between'>
      <Switch>

        <Route exact path="/">
          <Home />
        </Route>

        <Route path="/about">
          <About/>
        </Route>

        
        <Route path='/search'>
          <Search/>
        </Route>
        
        <Error/>

      </Switch>
>>>>>>> raiana
    </div>
  );
}

export default App;
