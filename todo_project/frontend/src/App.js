// import logo from './logo.svg';
import './App.css';
import React from "react";
import axios from "axios";

import UserList from "./components/User.js";
import Menu from "./components/Menu.js";
import Footer from "./components/Footer.js";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        // const users = [
        //     {
        //         'username': 'Alex',
        //         'first_name': 'alex',
        //         'last_name': 'geek',
        //         'email': 'test@gmail.com',
        //     },
        //     {
        //         'username': 'Alex_1',
        //         'first_name': 'alex_1',
        //         'last_name': 'geek_1',
        //         'email': 'test_1@gmail.com',
        //     },
        // ]
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState({'users': response.data})
        }).catch(error => {
            console.log(error)
        })
    }

    render() {
        return (
            <div>
                < Menu/>

                < UserList users={this.state.users}/>

                <Footer/>
            </div>
        )
    }
}

export default App;
