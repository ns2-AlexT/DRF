import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const Note = ({note}) => {
    return (
        <tr>
            <td>
                {note.name_of_project}
            </td>
            <td>
                {note.text_of_todo}
            </td>
            <td>
                {note.is_active_of_todo}
            </td>
            <td>
                {note.author_of_todo}
            </td>
        </tr>
    )
}

const NoteList = ({notes}) => {
    return (
        <div className="container">
            <hr/>
            <table className="header">
                <th>
                    Project name
                </th>
                <th>
                    Text of note
                </th>
                <th>
                    Status
                </th>
                <th>
                    Author
                </th>
            </table>
            <table className='container'>
                {notes.map((note_string) => <Note note={note_string}/>)}
            </table>
        </div>
    )
}
export default NoteList