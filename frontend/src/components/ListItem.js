import React from 'react'
import { Link } from 'react-router-dom'

let getLocalTime = (note) => {
	return new Date(note.updated).toLocaleDateString()
}

let getTitle = (note) => {
	let title = note.body.split('\n')[0]
	if (title.length > 15) {
		title.slice(0, 15)
	}

	return title
}

let getContent = (note) => {
	let title = note.body.split('\n')[0]
	let content = note.body.replaceAll('\n', '').replaceAll(title, '')
	if (content.length > 40) {
		return (content.slice(0, 40) + '...')
	}
	if (content.length == 0) {
		return ''
	}
	else
		return ('| ' + content)
}

// destructuring props: https://medium.com/@lcriswell/destructuring-props-in-react-b1c295005ce0
const ListItem = ( { note } ) => {
  return (
	<div>
		<Link to = {`/note/${note.id}/`}>
			<div className='notes-list-item'>
				<h4>{getTitle(note)}</h4>
				<p>
					<span>Last Update: { getLocalTime(note) }</span>
					<span>{ getContent(note) }</span>
				</p>
			</div>
		</Link>
	</div>
  )
}

export default ListItem