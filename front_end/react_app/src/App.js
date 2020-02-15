import React, { Component } from 'react';
import Header from  './components/layout/Header'
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
        completed: false
      }
    ]
  }
    //Toggle Complete
    markComplete = (id) =>{
      this.setState({ingredients: this.state.ingredients.map(ingredient => {
        if(ingredient.id === id){
          ingredient.completed = !ingredient.completed
        }
        return ingredient;
      })});
    }

    delIngredient = (id) => {
      
      this.setState({ ingredients: [...this.state.ingredients.filter(ingredient => ingredient.id !== id )]})
    
    }


  render(){
    return (

      <div className="App">

      <Header/>

      {/* //This is like calling the function/component */}
      <Ingredients ingredients = {this.state.ingredients} markComplete = {this.markComplete} delIngredient = {this.delIngredient}/>
      </div>

    );
  }
}

export default App;
