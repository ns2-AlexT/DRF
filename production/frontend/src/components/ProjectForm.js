import React from "react";


class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name_of_project: '', authors: []}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleChangeV2(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'authors': []
            })
            return;
        }
        let authors = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            console.log('=== ', event.target.selectedOptions.item(i).value)
            authors.push(event.target.selectedOptions.item(i).value)
        }
        console.log(authors.id)
        this.setState({'authors': authors})
        console.log('===', this.state.authors)
    }

    handleSubmit(event) {
        this.props.create_project(this.state.name_of_project, this.state.authors)
        console.log(this.state.name_of_project, ' **** ', this.state.authors)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">name</label>
                    <input type="text" className="form-control" name="name_of_project"
                           value={this.state.name_of_project}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <select name='authors' multiple onChange={(event) => this.handleChangeV2(event)}>
                    {this.props.authors.map((item) => <option value={item.id}> {item.username} </option>)}
                </select>
                <input type="submit" className="btn btn-primary" value="Save"/></form>
        );
    }
}

export default ProjectForm