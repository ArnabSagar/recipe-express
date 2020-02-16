import React, { Component } from 'react';
import { BrowserRouter as Router, Route} from 'react-router-dom'
import Header from  './components/layout/Header';
import AddIngredients from  './components/AddIngredients';
import Ingredients from './components/Ingredients';
import About from  './components/pages/About';
import Home from './components/pages/Home'
import uuid from  'uuid'
import './App.css';


class App extends Component{

  state = {
    ingredients:[
      {
        id:uuid.v4(),
        title: "Garlic",
        completed: false
      },
      {
        id:uuid.v4(),
        title: "Ginger",
        completed: false
      },
      {
        id:uuid.v4(),
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

    //Add Ingredient
    addIngredient = (title) =>{
      const newIngredient={
        id:uuid.v4(),
        title,
        completed: false
      }
       this.setState({ingredients: [...this.state.ingredients, newIngredient]})
    }
 

  render(){
    return (
      <Router>
        <div className="App">
          <div className  = "container">
          <Header/>
            <Route exact path="/" render={props => (
              <React.Fragment>
                  <AddIngredients addIngredient={this.addIngredient}  />
                  {/* includes the function call this.addIngredient */}
                  <div className ='itemsBox'>
                  {/* //This is like calling the function/ and passing arugments*/}
                  <Ingredients ingredients = {this.state.ingredients} markComplete = {this.markComplete} delIngredient = {this.delIngredient}/>
                  </div>

                  <button style = {btnStyle} >
                    COOK ME UP
                  </button>
                {/* ADD MAKE RECIPE BUTTON */}

              </React.Fragment>
            )} />
            <Route path = "/about" component={About}/>
            <Route path = "/home" component={Home}/>
          </div>
        </div>
      </Router>

    );
  }
}


const btnStyle = {

  color: "Black",
  backgroundColor: '#45a13f',
  border: '1px solid black',
  borderRadius: '10px',
  height: '50px',
  width: '120px',
  marginBottom: '5%',
  textAlign: 'center'
  

}

export default App;
