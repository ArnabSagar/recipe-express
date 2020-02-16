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
            <div className='specificItem' style={this.getStyle()}>
                <p>
                    
                    {title}
                    <button style={btnStyle} onClick = {this.props.delIngredient.bind(this, id)}>x</button>
                </p>
            </div>
        )
    }
}

//PropTypes
IndividualIngredient.propTypes = {
    ingredient: PropTypes.object.isRequired
}

const btnStyle = {

    backgroundColor: '#fff',
    color: '#ff0000',
    border: 'none',
    padding: '5px 9px',
    borderRadius: '50%',
    cursor: 'pointer',
    float: 'right'

}
// const itemStyle = {
//     backgroundColor: '#f4f4f4'
// }


export default IndividualIngredient
