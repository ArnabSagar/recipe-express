import React, { Component } from 'react'

export class AddIngredients extends Component {
    render() {
        return (
            <form style = {{display: 'flex'}}>
                <input
                    type = 'text'
                    name = 'title'
                    style = {{flex: '10', padding: '5px'}}
                    placeholder="Add Ingredient..."
                />
                <input
                    type = "submit"
                    value = "Submit"
                    className = "btn"
                    style = {{flex: '1'}}
                />
            </form>
        )
    }
}

export default AddIngredients