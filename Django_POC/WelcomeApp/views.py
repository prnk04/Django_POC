from django.shortcuts import render
from django import forms

from .models import ImgResource



# Create your views here.

# creating search form here
class NewSearchForm(forms.Form):
    search = forms.CharField(label = '', widget= forms.TextInput(attrs={'placeholder':'Search Resource'}))

# fetching data from db



def homePage(request):
    if request.method == 'POST':
        searchForm = NewSearchForm(request.POST)
        if searchForm.is_valid():
            searchedText = searchForm.cleaned_data['search']
            print(searchedText)
        else:
            print(searchForm)
    return render(request, 'WelcomeApp/index.html', {'searchForm': NewSearchForm()})

def findPage(request, queryName):
    resrc = ''
    resCount = 0
    if queryName.capitalize() == 'Image' or queryName.capitalize == 'Images':
        resrc = ImgResource.objects.all()
        resCount = ImgResource.objects.count()
    return render(request, 'WelcomeApp/resourcePage.html', {'resourceName': queryName.capitalize(), 'searchForm': NewSearchForm(),
                    'resource': resrc, 'resCount':resCount})


