import React, { Component } from 'react';
import IndividualIngredient from './IndividualIngredient'
import PropTypes from 'prop-types'

class Ingredients extends Component {
    
  
    
    render(){

        //the map function can return an array from an array
        //we are running a for each loop here whereby we are mapping through single 'ingredient's

        // console.log(this.props.ingredients)
        
        return this.props.ingredients.map((ingredient) => (
            <IndividualIngredient key={ingredient.id} ingredient = {ingredient} markComplete = {this.props.markComplete} />
        ));
    }
}

//PropTypes
Ingredients.propTypes = {
    ingredients: PropTypes.array.isRequired
}

export default Ingredients;
