import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class Navbar extends Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <nav className="navbar navbar-dark bg-dark navbar-expand-lg">
                <Link to="/" className="navbar-brand">AutoRack</Link>
                <div className="collapse navbar-collapse">
                <ul className="navbar-nav mr-auto">
                    <li className="navbar-nav mr-auto">
                    <Link to="/inventory" className="nav-link">Inventory</Link>
                    </li>
                    <li className="navbar-nav mr-auto">
                    <Link to="/manageMenu" className="nav-link">Manage Menu</Link>
                    </li>
                    <li className="navbar-nav mr-auto">
                    <Link to="/messages" className="nav-link">Messages</Link>
                    </li>
                    <li className="navbar-nav mr-auto">
                    <Link to="/restockPurchases" className="nav-link">Restock RestockPurchases</Link>
                    </li>
                </ul>
                </div>
            </nav>
        );
    }
}