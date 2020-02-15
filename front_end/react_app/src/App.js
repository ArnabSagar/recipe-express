import React, { Component } from 'react';
import Ingredients from './components/Ingredients'
import './App.css';

class App extends Component{

  state = {
    ingredients:[
      {
        id:1,
        title: "Garlic",
        completed: false
      },
      {
        id:2,
        title: "Ginger",
        completed: false
      },
      {
        id:3,
        title: "Rice",
        completed: true
      }
    ]
  }

    markComplete = (id) =>{
      console.log(id)
    }

  render(){

    return (

      <div className="App">
      {/* //This is like calling the function/component */}
      <Ingredients ingredients = {this.state.ingredients} markComplete = {this.markComplete}/>
      </div>

    );
  }
}

export default App;
