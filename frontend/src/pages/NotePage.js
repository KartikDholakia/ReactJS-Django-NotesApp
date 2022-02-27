import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom';
import { ReactComponent as ArrowLeft } from '../assets/chevron-left.svg'

const NotePage = () => {

	const noteId = useParams().id

	const [note, setNote] = useState(null)

	let navigate = useNavigate()

	useEffect(() => {
		getNote()
	}, [noteId])

	let getNote = async () => {
		if (noteId === 'new')	return

		let response = await fetch(`/api/notes/${noteId}/`)
		let data = await response.json()
		setNote(data)
	}

	let updateNote = async () => {
		fetch(`/api/notes/${noteId}/`, {
			method: "PUT",
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(note)
		})
	}

	let createNote = async () => {
		fetch(`/api/notes/`, {
			method: "POST",
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(note)
		})
	}

	let hanldeSubmit = () => {
		// if note body is empty then delete that note
		if (noteId !== 'new' && note.body === '') {
			// console.log('Case-1')
			deleteNote()
		}
		else if (noteId !== 'new') {
			// console.log('Case-2')
			updateNote()
		}
		else if (noteId === 'new' && note.body != null) {
			// console.log('Case-3')
			createNote()
		}
		navigate('/')
	}

	let deleteNote = async () => {
		fetch(`/api/notes/${noteId}/`, {
			method: "DELETE",
			headers: {
				'Content-Type': 'application/json'
			}
		})
		navigate('/')
	}

	return (
		<div className='note'>
			<div className='note-header'>
				<h3>
					<ArrowLeft onClick={hanldeSubmit}/>
				</h3>
				{noteId !== 'new' ? (
					<button onClick={deleteNote}>Delete</button>
				) : (
					<button onClick={hanldeSubmit}>Done</button>
				)}
				
			</div>
			<textarea
				onChange={(e) => {
					setNote({...note, 'body': e.target.value}) 
					// console.log(note)
				}}
				value={note?.body}></textarea>
		</div>
	)
}

export default NotePage