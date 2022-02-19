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
import NotesOfProject from "./components/NotesOfProject";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'notes': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState({'users': response.data})
        }).catch(error => {
            console.log(error)
        })
        axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
            this.setState({'projects': response.data})
        }).catch(error => {
            console.log(error)
        })
        axios.get('http://127.0.0.1:8000/api/notes/').then(response => {
            this.setState({'notes': response.data})
        }).catch(error => {
            console.log(error)
        })
    }

    render() {
        return (
            <div>

                <BrowserRouter>

                    < Menu/>

                    <Switch>

                        < Route exact path='/' component={() => <UserList users={this.state.users}/>}/>

                        < Route exact path='/projects/'
                                component={() => <ProjectList projects={this.state.projects}/>}/>

                        < Route path='/project/:id'> <NotesOfProject notes={this.state.notes}/> </Route>

                        < Route exact path='/notes/' component={() => <NoteList notes={this.state.notes}/>}/>

                        < Route component={Error404}/>

                    </Switch>

                </BrowserRouter>

                <Footer/>

            </div>
        )
    }
}

export default App;
