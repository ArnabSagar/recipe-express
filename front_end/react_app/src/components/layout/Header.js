import React from 'react'
import { Link } from 'react-router-dom'

function Header() {  //This is a functional component
    return (
        <header style={headerStyle}>
            <Link to="/home">
            <img src="./LOGO.png" height='150px' width = '400px' alt="Recipe Express Logo"></img>
            </Link> <br></br>
            
            <Link style = {linkStyle} to = "/home">Home</Link> | <Link style = {linkStyle} to = "/">Cook </Link>
            | <Link style = {linkStyle} to = "/about" >About</Link>
        </header>
    )
}

    const headerStyle = {
        background: 'white',
        color: 'white',
        padding: '10px',
        textAlign: 'center',
        cursor: 'pointer'
    }

    const linkStyle = {
        color: 'black',
        fontSize: 25,
        textDecoration: 'none'
    }

export default Header;