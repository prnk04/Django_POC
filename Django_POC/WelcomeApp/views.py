from django.shortcuts import render
from django import forms

from .models import ImgResource, VideoResource, ArticleResource

from django.db.models import Q



# Create your views here.

# creating search form here
class NewSearchForm(forms.Form):
    search = forms.CharField(label = '', widget= forms.TextInput(attrs={'placeholder':'Search Resource'}))

# fetching data from db



def homePage(request):
    queryResult = {}
    if request.method == 'POST':
        searchForm = NewSearchForm(request.POST)
        if searchForm.is_valid():
            searchedText = searchForm.cleaned_data['search']
            queryResult = getResource(searchedText)
            return render(request, 'WelcomeApp/index.html', {'searchForm': NewSearchForm(), 'queryResult':queryResult})
        else:
            print(searchForm)
    return render(request, 'WelcomeApp/index.html', {'searchForm': NewSearchForm(),'queryResult':queryResult})

def findPage(request, queryName):
    resrc = ''
    resCount = 0

    if request.method == 'POST':
        searchForm = NewSearchForm(request.POST)
        if searchForm.is_valid():
            searchedText = searchForm.cleaned_data['search']
            queryResult = getResource(searchedText)
            return render(request, 'WelcomeApp/resourcePage.html', {'searchForm': NewSearchForm(), 'queryResult':queryResult, 
                            'resourceName': '', 'resource': resrc, 'resCount':resCount})
        else:
            print(searchForm)

    if queryName.capitalize() == 'Image' or queryName.capitalize() == 'Images':
        resrc = ImgResource.objects.all()
        resCount = ImgResource.objects.count()
    if queryName.capitalize() == 'Video' or queryName.capitalize() == 'Videos':
        resrc = VideoResource.objects.all()
        resCount = VideoResource.objects.count()
    if queryName.capitalize() == 'Article' or queryName.capitalize() == 'Articles':
        resrc = ArticleResource.objects.all()
        resCount = ArticleResource.objects.count()

    return render(request, 'WelcomeApp/resourcePage.html', {'resourceName': queryName.capitalize(), 'searchForm': NewSearchForm(),
                    'resource': resrc, 'resCount':resCount})


def getResource(searchedText):
    articleResources =  ArticleResource.objects.filter(Q(resource_name__contains = searchedText) | Q(authors__contains = searchedText)
                        | Q(keywords__contains = searchedText) | Q(link__contains = searchedText) | Q(resourceFile__contains = searchedText))

    imagesResources = ImgResource.objects.filter(Q(resource_name__contains = searchedText) | Q(authors__contains = searchedText)
                        | Q(keywords__contains = searchedText) | Q(link__contains = searchedText) | Q(resourceFile__contains = searchedText))
    
    VideoResources = VideoResource.objects.filter(Q(resource_name__contains = searchedText) | Q(authors__contains = searchedText)
                        | Q(keywords__contains = searchedText) | Q(link__contains = searchedText) | Q(resourceFile__contains = searchedText))

    queryResult= {'Articles':articleResources, 
                   'Images':imagesResources ,
                   'Videos':VideoResources}

    return queryResult