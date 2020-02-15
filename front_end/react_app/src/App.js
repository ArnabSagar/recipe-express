import React, { Component } from 'react';
import Todos from './components/Todos'
import './App.css';

class App extends Component{

  state = {
    todos:[
      {
        id:1,
        title: "diiner",
        completed: false
      },
      {
        id:2,
        title: "trash",
        completed: false
      },
      {
        id:3,
        title: "dance",
        completed: false
      }
    ]
  }

  render(){

    return (
      <div className="App">
        <Todos todos = {this.state.todos}/>

            <div id="myDIV" class="header">
            <h2>My To Do List</h2>
            <input type="text" id="myInput" placeholder="Title..."></input>
            <span onclick="newElement()" class="addBtn">Add</span>
            </div>

          <ul id="myUL">
            <li>Hit the gym</li>
            <li class="checked">Pay bills</li>
            <li>Meet George</li>
            <li>Buy eggs</li>
            <li>Read a book</li>
            <li>Organize office</li>
          </ul>

      </div>

    );
  }
}

export default App;
