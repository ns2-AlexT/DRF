import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

class UserLoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'user_login': '',
            'user_pass': ''
        }
    }

    HandleFormUserLogin(event) {
        this.setState({
                [event.target.name]: event.target.value
            }
        );
    }

    HandleFormSubmit(event) {
        this.props.getToken(this.state.user_login, this.state.user_pass)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.HandleFormSubmit(event)}>
                <input type="text" name="user_login" placeholder="user_login" value={this.state.user_login}
                       onChange={(event) => this.HandleFormUserLogin(event)}/>
                <input type="password" name="user_pass" placeholder="user_pass" value={this.state.user_pass}
                       onChange={(event) => this.HandleFormUserLogin(event)}/>
                <input type='submit' value='Login'/>
            </form>
        )
    }
}

export default UserLoginForm