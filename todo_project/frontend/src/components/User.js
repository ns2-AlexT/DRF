import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const User = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <div className="container">
            <hr/>
            <table className="header">
                <th>
                    User name
                </th>
                <th>
                    First name
                </th>
                <th>
                    Last name
                </th>
                <th>
                    Email
                </th>
            </table>
            <table className='container'>
                {users.map((user_string) => <User user={user_string}/>)}
            </table>
        </div>
    )
}
export default UserList