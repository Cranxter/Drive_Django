from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.


def home(request):
	title="This is a title"
	form=SignUpForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		print (instance)
		


	context={
	"template_title":title,
	"form":form
	}

	return render(request,"home.html",context)

