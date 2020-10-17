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
    </div>
  );
}

export default App;
