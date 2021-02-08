from django.shortcuts import render
from django import forms

import markdown2


import os

# Create your views here.

# creating search form here
class NewSearchForm(forms.Form):
    search = forms.CharField(label = '', widget= forms.TextInput(attrs={'placeholder':'Search Resource'}))



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
    return render(request, 'WelcomeApp/resourcePage.html', {'resourceName': queryName.capitalize(), 'searchForm': NewSearchForm()})


