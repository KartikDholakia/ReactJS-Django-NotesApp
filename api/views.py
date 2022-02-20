from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from api import serializers

# Create your views here.

# decorators: (so as to use functions instead of classes) (django rest style of view)
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
	notes = Note.objects.all().order_by('-updated')  # this returns the list of python objects
	# notes will be ordered in decreasing order of update date
	serial_class = NoteSerializer(notes, many=True)     # many=True means that we want to serialize multiple objects
	
	return Response(serial_class.data)

@api_view(['GET'])
def getNote(request, pk):
	note = Note.objects.get(id=pk)
	serial_class = NoteSerializer(note, many=False)
	
	return Response(serial_class.data)

# PUT -> used to update
# POST -> used to create new entry
@api_view(['PUT'])
def updateNote(request, pk):
	data = request.data		# we have access to request.data thru django rest framework
	note = Note.objects.get(id=pk)

	# this will serialize the existing 'note' with data
	serializer = NoteSerializer(instance=note, data=data)

	# save to database:
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
	note = Note.objects.get(id=pk)
	note.delete()

	return Response('Note was Deleted!!')