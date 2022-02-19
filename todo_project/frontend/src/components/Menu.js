import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link} from "react-router-dom";

const Menu = () => {
    return (
        <nav>
            <ul className="header">
                <li>
                    <Link to='/'>
                        Users
                    </Link>
                </li>
                <li>
                    <Link to='/projects/'>
                        Projects
                    </Link>
                </li>
                <li>
                    <Link to='/notes/'>
                        Tasks
                    </Link>
                </li>
                <li>
                        Log in
                </li>
            </ul>
        </nav>
    )
}

export default Menu