import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from "react-router-dom";


export default function Menu({status, logout}) {

    let button = ''
    if (status.is_in) {
        button = <button onClick={logout}> {status.user} Logout</button>
    } else {
        button = <Link to='/login/'>Login</Link>
    }

    return (
        <nav>
            <ul className="header">
                <li>
                    <Link to='/'>
                        Users
                    </Link>
                </li>
                <li>
                    <Link to='/projects'>
                        Projects
                    </Link>
                </li>
                <li>
                    <Link to='/notes'>
                        Tasks
                    </Link>
                </li>
                <li>
                    {button}
                </li>
            </ul>
        </nav>
    )
}
