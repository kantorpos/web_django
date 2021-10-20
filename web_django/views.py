from django.shortcuts import render

def index(request):
	context = {
		'Judul':'Home Page',
		'Content':'Ini adalah home page web Django'

	}

	return render(request, 'index.html',context)