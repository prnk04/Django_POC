from django.shortcuts import render
from django import forms

import markdown2
import resources

import os

# Create your views here.

# creating search form here
class NewSearchForm(forms.Form):
    search = forms.CharField(label = '', widget= forms.TextInput(attrs={'placeholder':'Search Resource'}))

# creating resource addition form
class NewResourceForm(forms.Form):
    title = forms.CharField(label = 'Title', widget = forms.TextInput(attrs={'class': 'titleAdd'}))
    entry = forms.CharField(label = 'Enter text here', widget = forms.Textarea(
                                                                attrs={'class': 'entryAdd','cols':50,'rows':10, 'height':'auto'}))

def homePage(request):
    return render(request, 'WelcomeApp/index.html', {'searchForm': NewSearchForm()})

def findPage(request, queryName):
    return render(request, 'WelcomeApp/resourcePage.html', {'resourceName': queryName.capitalize(), 'searchForm': NewSearchForm()})

# need to work on saving data

def addContent(request):
    if request.method == 'POST':
        formData = NewResourceForm(request.POST)
        if formData.is_valid():
            title = formData.cleaned_data["title"]
            content = formData.cleaned_data["entry"]
            print(title, " : ", content)
            writeData(title, content)

        else:
            print(formData)

    return render(request, 'WelcomeApp/addPage.html', {'searchForm': NewSearchForm(), 'NewResourceForm': NewResourceForm})

def writeData(title, content):
    print(os.getcwd())
    fileName = '././resources/'+title+'.md'
    with open(fileName) as f:
        f.write(content)
