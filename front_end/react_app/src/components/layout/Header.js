import React from 'react'

function Header() {  //This is a functional component
    return (
        <header style={headerStyle}>
            <h1>Recipe Express</h1>
        </header>
    )
}

    const headerStyle = {
        background: '#333',
        color: 'white',
        padding: '10px',
        textAlign: 'center'
    }


export default Header;