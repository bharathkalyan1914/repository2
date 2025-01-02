from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
	#ss ----> is html-data/code
	ss = '''		
			<center>
				<h2 style="color:Blue;">
					Hello User, Welcome to Django First-Project First-App
				</h2>
                <h1>hello bharath in git-view</h1>
		<h3>hello bharath kalyan welcome to the "github" </h3>
				<hr />
			</center>
		''';
	
	return HttpResponse(ss);

