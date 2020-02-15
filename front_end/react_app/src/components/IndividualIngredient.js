import React, { Component } from 'react';
import PropTypes from 'prop-types';

export class IndividualIngredient extends Component {

    getStyle = () => {

        return{
            backgroundColor: '#f4f4f4',
            padding: '10px',
            borderBottom: '1px #ccc dotted',
            textDecoration: this.props.ingredient.completed ? 'line-through' : 'none'
        }
    }

    render() {

        const{id, title} =  this.props.ingredient
        return (
            <div style={this.getStyle()}>
                <p>
                    <input type = "checkbox" onChange={this.props.markComplete.bind(this, id)}/>{'  '}
                    {title}
                </p>
            </div>
        )
    }
}

//PropTypes
IndividualIngredient.propTypes = {
    ingredient: PropTypes.object.isRequired
}


// const itemStyle = {
//     backgroundColor: '#f4f4f4'
// }


export default IndividualIngredient
