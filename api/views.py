from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

# decorators:
@api_view(['GET'])      # takes the list of http methods (get, post, put, ...)

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

# to get notes from the database
# in order to render the python objects, we first need to serialize them
# NOTE: You can add error handling here:
@api_view(['GET'])
def getNotes(request):
	notes = Note.objects.all()  # this returns the list of python objects
	serial_class = NoteSerializer(notes, many=True)     # many=True means that we want to serialize multiple objects
	
	return Response(serial_class.data)

@api_view(['GET'])
def getNote(request, pk):
	note = Note.objects.get(id=pk)
	serial_class = NoteSerializer(note, many=False)
	
	return Response(serial_class.data)    