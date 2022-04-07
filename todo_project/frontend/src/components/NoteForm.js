import React from "react";


class NoteForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            project_id: window.location.search.replace('?id_project=', ''),
            text_of_note: ''
        }
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value})
    }

    handleSubmit(event) {
        this.props.create_note(this.state.project_id, this.state.text_of_note)
        console.log(this.state.project_id, ' **** ', this.state.text_of_note)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">name</label>
                    <input type="text" className="form-control" name="text_of_note"
                           value={this.state.text_of_note}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <input type="submit" className="btn btn-primary" value="Save"/></form>
        );
    }
}

export default NoteForm