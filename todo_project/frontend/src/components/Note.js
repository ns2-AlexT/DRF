import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const Note = ({note, delete_note}) => {
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
            <td>
                <button onClick={()=>delete_note(note.id)} type={'button'}>delete</button>
            </td>
        </tr>
    )
}

const NoteList = ({notes, delete_note}) => {
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
                {notes.map((note_string) => <Note note={note_string} delete_note={delete_note}/>)}
            </table>
        </div>
    )
}
export default NoteList