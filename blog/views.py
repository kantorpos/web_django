from django.shortcuts import render

def index(request):
	context = {
		'Judul':'Home Blog',
		'Content':'Ini adalah home blog'
	}

	return render(request, 'blog/index.html',context)