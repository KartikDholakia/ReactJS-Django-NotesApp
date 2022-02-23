from turtle import update
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from api import serializers
from .utils import updateNote, getSingleNote, deleteNote, getNotesList, createNote

"""
Routes For RESTful APIs:
/notes GET
/notes POST
/notes/<id> GET
/notes/<id> PUT
/notes/<id> DELETE

HTTP Methods:
GET -> to fecth data
PUT -> used to update
POST -> used to create new entry
DELETE -> to delete a record
"""

# decorators: (so as to use functions instead of classes) (django rest style of view)
# takes the list of acceptable http methods (get, post, put, ...)
@api_view(['GET'])
def getRoutes(request):
	
	routes = [
		{
			'Endpoint': '/notes/',
			'method': 'GET',
			'body': None,
			'description': 'Returns an array of notes'
		},
		{
			'Endpoint': '/notes/id',
			'method': 'GET',
			'body': None,
			'description': 'Returns a single note object'
		},
		{
			'Endpoint': '/notes/create/',
			'method': 'POST',
			'body': {'body': ""},
			'description': 'Creates new note with data sent in post request'
		},
		{
			'Endpoint': '/notes/id/update/',
			'method': 'PUT',
			'body': {'body': ""},
			'description': 'Creates an existing note with data sent in post request'
		},
		{
			'Endpoint': '/notes/id/delete/',
			'method': 'DELETE',
			'body': None,
			'description': 'Deletes and exiting note'
		},
	]

	return Response(routes)

# Notes -> to get the list of notes from the database and to create a note
# in order to render the python objects, we first need to serialize them
# NOTE: You can add error handling here:
@api_view(['GET', 'POST'])
def Notes(request):

	if request.method == 'GET':
		return getNotesList()

	if request.method == 'POST':
		return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

	if request.method == 'GET':
		return getSingleNote(request, pk)

	if request.method == 'PUT':
		return updateNote(request, pk)

	if request.method == 'DELETE':
		return deleteNote(pk)