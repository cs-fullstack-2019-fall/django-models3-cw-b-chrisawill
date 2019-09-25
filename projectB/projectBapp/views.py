from django.shortcuts import render

# Create your views here.

# You need to import Books from models
from django.http import HttpResponse
def library(request):
    return HttpResponse('hello')





def allbooks(request):
    tempstrings = ""
    booklist = books.objects.all()  #You need to matchs "books" to your model or what you import it as
    for eachbook in booklist:
        tempstrings = tempstrings + eachbook + "."   #you cannot combine a string with data from a model. You need to turn eachbook into a string and then you need to ask for a piece of information like name or page number. Then it will return the book as a Visible string information
    return HttpResponse(tempstrings)


def addBook():   #you need to define request
    getallbooksfromdatabase = Books.objects.all   #you need to add parenthesis to the end of "all"
    for eachbook in getallbooksfromdatabase:
        print(eachbook)
    return HttpResponse("All books")
def fictionbooks(request)   #you need to have a colon at the end of the parenthesis
    getallbooksfromdatabase = Books.objects.all  # you need parenthesis at the end of "all"
    for eachbook in getallbooksfromdatabase:
        if(eachbook.works == "fiction"):
            print(eachbook)
        return HttpResponse("All Books")