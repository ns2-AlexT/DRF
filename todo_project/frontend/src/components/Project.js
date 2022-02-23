import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link} from "react-router-dom";

const Project = ({project}) => {
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
        </tr>
    )
}

const ProjectList = ({projects}) => {
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
                {projects.map((project_string) => <Project project={project_string}/>)}
            </table>
        </div>
    )
}
export default ProjectList