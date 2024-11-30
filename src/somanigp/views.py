# views : contains actual functions responsible for rendering html and where to fetch html.
from django.http import HttpResponse
from django.shortcuts import render  # Exists in .http also but this is used
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    """Returns html page to render"""
    title = "Home Page"
    # queryset = PageVisit.objects.all()  # Getting all objects created of this class.#  ** List of objects. 
    page_qs = PageVisit.objects.filter(path=request.path)  # Applying filter to get specific data
    page_visit_count = page_qs.count()
    my_context = {
        "page_title": title,
        "queryset": page_qs,
        "page_visit_count": page_visit_count,
        "total_visits_count": PageVisit.objects.all().count()
    }
    html_template = "home.html"
    # print(request.user)  # AnonymousUser
    # Django tried loading these templates, in this order: !NOTE : Can add dir to search in settings.py
    # \site-packages\django\contrib\admin\templates\home.html (Source does not exist)
    # \.venv\Lib\site-packages\django\contrib\auth\templates\home.html (Source does not exist)

    PageVisit.objects.create(path=request.path)  # Creating an object of the class. Storing data in db.
    # path field value will come here. If not passed anything then it will be empty which is allowed.
    
    return render(request, html_template, my_context)  # * will apply my_context to base html files too, from which current html file may extend.


def old_home_page_view(request, *args, **kwargs):
    """Returns html page to render"""
    # print("request is" +str(request))  # request is<WSGIRequest: GET '/hellow-world/'>
    # args - tuple and kwargs - dict

    print(this_dir)  # D:\Govind's Library\projects\django-project\src\somanigp
    html_file_path = this_dir/"home.html"
    # html_ = html_file_path.read_text()  # reads the file and saves content in html_

    my_title = "Govind's Page"
    my_context = {
        "page_title": my_title
    }
    my_html_ = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>

        <h1>Hello from {page_title}!</h1>

        <p>This is a paragraph of text.</p>

    </body>
    </html>
    """.format(**my_context)
    # return HttpResponse("<h1>Hello World</h1>")  # Takes http content to render as input.
    return HttpResponse(my_html_)