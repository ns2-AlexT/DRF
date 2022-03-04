// import logo from './logo.svg';
import './App.css';
import React from "react";
import axios from "axios";
import {Route, BrowserRouter, Switch} from "react-router-dom";


import Menu from "./components/Menu.js";
import UserList from "./components/User.js";
import ProjectList from "./components/Project.js";
import NoteList from "./components/Note.js";
import Footer from "./components/Footer.js";
import Error404 from "./components/Error404.js";
import NotesOfProject from "./components/NotesOfProject.js";
import UserLoginForm from "./components/AppForLoginUser.js";
import Cookies from "universal-cookie/es6";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'notes': [],
            'status_of_auth': {'user': '', 'is_in': false, 'token': ''}
        }
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        headers['Authorization'] = `Token ${this.state.status_of_auth.token}`
        return headers
    }

    load_all_data_on_start() {
        console.log('load all data start')
        const headers = this.get_headers()
        console.log('getting headers ' + headers['Authorization'])

        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
            this.setState({'users': response.data})
        }).catch(error => {
            console.log(error)
        })
        axios.get('http://127.0.0.1:8000/api/projects/', {headers}).then(response => {
            this.setState({'projects': response.data})
        }).catch(error => {
            console.log(error)
        })
        axios.get('http://127.0.0.1:8000/api/notes/', {headers}).then(response => {
            this.setState({'notes': response.data})
        }).catch(error => {
            console.log(error)
        })
    }

    let_logout() {
        console.log('Clearing data')
        this.setState({'notes': []})
        this.setState({'user': []})
        this.setState({'projects': []})
        this.setState({
            'status_of_auth': {
                'user': '',
                'token': '',
                'is_in': false
            }
        }, () => this.load_all_data_on_start())
    }

    set_token_to_cook_state(token, user_login) {
        const cookie = new Cookies()
        cookie.set('token', token)
        this.setState({
                'status_of_auth':
                    {'user': user_login, 'is_in': true, 'token': token}
            },
            () => this.load_all_data_on_start())
        console.log('is_in ' + this.state.status_of_auth.is_in)
        // document.cookie = `token=${token}`
    }

    get_token_from_cookie() {
        const cookie_from = new Cookies()
        const token = cookie_from.get('token')
        this.setState({'status_of_auth': {'token': token}}, () => this.load_all_data_on_start())
    }

    get_token_from_backend(user_login, user_pass) {
        axios.post('http://localhost:8000/api-token-auth/',
            {username: user_login, password: user_pass}).then(response => {
            this.set_token_to_cook_state(response.data['token'], user_login)
        }).catch(error => {
            console.log(error)
        })
    }


    componentDidMount() {
        if (this.state.status_of_auth.is_in) {
            this.get_token_from_cookie()
        }
    }

    render() {
        return (
            <div>

                <BrowserRouter>

                    < Menu status={this.state.status_of_auth} logout={() => this.let_logout()}/>
                    <Switch>

                        < Route exact path='/' component={() => <UserList users={this.state.users}/>}/>

                        < Route exact path='/projects/'
                                component={() => <ProjectList projects={this.state.projects}/>}/>

                        < Route path='/project/:id'> <NotesOfProject notes={this.state.notes}/> </Route>

                        < Route exact path='/notes/' component={() => <NoteList notes={this.state.notes}/>}/>

                        < Route exact path='/login/'
                                component={() => <UserLoginForm
                                    getToken={(user_login, user_pass) =>
                                        this.get_token_from_backend(user_login, user_pass)}
                                />}/>

                        < Route component={Error404}/>


                    </Switch>

                </BrowserRouter>

                <Footer/>

            </div>
        )
    }
}

export default App;
