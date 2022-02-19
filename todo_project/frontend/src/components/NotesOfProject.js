import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {useParams} from "react-router-dom";

const Note = ({note}) => {
    return (
        <tr>
            <td>
                {note.text_of_todo}
            </td>
            <td>
                {note.author_of_todo}
            </td>
            <td>
                {note.is_active_of_todo}
            </td>
        </tr>
    )
}

const NotesOfProject = ({notes}) => {
    let {id} = useParams()
    let filtered_notes = notes.filter(note => note.name_of_project === (parseInt(id)))
    //Так и не смог заставить работать includes - выходит ошибка:
    // Uncaught TypeError: note.name_of_project.includes is not a function
    // let filtered_notes_1 = notes.filter((note => note.name_of_project.includes(parseInt(id))))

    return (
        <div className="container">
            <hr/>
            <table className="header">
                <th>
                    Text of note
                </th>
                <th>
                    Author_of_todo
                </th>
                <th>
                    Status
                </th>
            </table>
            <table className='container'>
                {filtered_notes.map((note_string) => <Note note={note_string}/>)}
            </table>
        </div>
    )
}

export default NotesOfProject