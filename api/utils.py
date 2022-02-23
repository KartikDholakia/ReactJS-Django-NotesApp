"""
utils.py has all the functions that are used in views.py
"""

from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def getSingleNote(pk):
	note = Note.objects.get(id=pk)
	serial_class = NoteSerializer(note, many=False)
	return Response(serial_class.data)


def getNotesList():
	notes = Note.objects.all().order_by('-updated') # this returns the list of python objects
													# notes will be ordered in decreasing order
													# of update date

	serial_class = NoteSerializer(notes, many=True) # many=True means that we want to serialize 
													# multiple objects		
	return Response(serial_class.data)


def createNote(request):
	data = request.data								# it will return json object
	note = Note.objects.create(
		body=data['body']
		# 'created' and 'updated' field will automatically get data from models
	)

	serializer = NoteSerializer(note, many=False)
	return Response(serializer.data)


def updateNote(request, pk):
		data = request.data							# we have access to request.data thru 
													# django rest framework
		note = Note.objects.get(id=pk)

		# this will serialize the existing 'note' with data
		serializer = NoteSerializer(instance=note, data=data)

		# save to database:
		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)


def deleteNote(pk):
	note = Note.objects.get(id=pk)
	note.delete()
	return Response('Note was Deleted!!')
