import React, { Component } from 'react'

export class AddIngredients extends Component {

    state = {
        title: ''
    }

    onSubmit = (e) => {
        e.preventDefault();
        this.props.addIngredient(this.state.title);
        this.setState({title: ''});

    }
    onChange = (e) => this.setState({[e.target.name]: e.target.value});

    render() {
        return (
            <form onSubmit={this.onSubmit} style = {{display: 'flex'}}>
                <input
                    type = "text"
                    name = "title"
                    style = {{flex: '10', padding: '5px'}}
                    className = "addIngredientsBox"
                    placeholder="Add Ingredient..."
                    value = {this.state.title}
                    onChange = {this.onChange}
                />
                <input
                    type = "submit"
                    value = "Add Item"
                    className = "btn"
                    style = {{flex: '1'}}
                />
            </form>
        )
    }
}

export default AddIngredients
