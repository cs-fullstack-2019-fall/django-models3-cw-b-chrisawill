from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def library(request):
    return HttpResponse('hello')





def allbooks(request):
    tempstrings = ""
    booklist = books.objects.all()
    for eachbook in booklist:
        tempstrings = tempstrings + eachbook + "."
    return HttpResponse(tempstrings)


def addBook():
    getallbooksfromdatabase = Books.objects.all
    for eachbook in getallbooksfromdatabase:
        print(eachbook)
    return HttpResponse("All books")
def fictionbooks(request)
    getallbooksfromdatabase = Books.objects.all
    for eachbook in getallbooksfromdatabase:
        if(eachbook.works == "fiction"):
            print(eachbook)
        return HttpResponse("All Books")