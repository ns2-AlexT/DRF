import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from "react-router-dom";

const Project = ({project, delete_project}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}`}>{project.name_of_project}</Link>
            </td>
            <td>
                {project.link_to_repo}
            </td>
            <td>
                {project.list_of_users}
            </td>
            <td>
                <button onClick={() => delete_project(project.id)} type={'button'}>delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, delete_project}) => {
    return (
        <div className="container">
            <hr/>
            <table className="header">
                <th>
                    Project name
                </th>
                <th>
                    Link to git
                </th>
                <th>
                    Users list
                </th>
                <th>
                    Email
                </th>
            </table>
            <table className='container'>
                {projects.map((project_string) => <Project project={project_string}
                                                           delete_project={delete_project}/>)}
            </table>
            <Link to={'/projects/create'}>New project</Link>
        </div>
    )
}
export default ProjectList