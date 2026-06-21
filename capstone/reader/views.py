from django.shortcuts import render

# Create your views here.
def index(request):
    mock_books = [
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
    ]
    
    genres = [
        {"genre": "romance", "icon": "bi-heart-fill"},
        {"genre": "fantasy", "icon": "bi-stars"},
        {"genre": "sci-fi", "icon": "bi-rocket-takeoff"},
        {"genre": "mystery", "icon": "bi-search"},
        {"genre": "thriller", "icon": "bi-lightning-charge"},
        {"genre": "horror", "icon": "bi-ghost"},
        {"genre": "historical fiction", "icon": "bi-hourglass-split"},
        {"genre": "biography", "icon": "bi-person-badge"},
        {"genre": "self-help", "icon": "bi-lightbulb"},
        {"genre": "adventure", "icon": "bi-compass"}
    ]

    return render(request, "reader/index.html", {
        "books": mock_books,
        "genres": genres,
    })

def discover(request):
    return render(request, "reader/discover.html")

def mylibrary(request):
    return render(request, "reader/mylibrary.html")

def readinglists(request):
    return render(request, "reader/readinglists.html")

def savedquote(request):
    return render(request, "reader/savedquote.html")

def profile(request):
    mock_books = [
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
        {
            "title": "Home",
            "author": "Joy Alinsky",
            "genre": "romance",
            "reads": "15M",
            "image": "reader/home.png"
        },
    ]
    
    genres = [
        {"genre": "romance", "icon": "bi-heart-fill"},
        {"genre": "fantasy", "icon": "bi-stars"},
        {"genre": "sci-fi", "icon": "bi-rocket-takeoff"},
        {"genre": "mystery", "icon": "bi-search"},
        {"genre": "thriller", "icon": "bi-lightning-charge"},
        {"genre": "horror", "icon": "bi-ghost"},
        {"genre": "historical fiction", "icon": "bi-hourglass-split"},
        {"genre": "biography", "icon": "bi-person-badge"},
        {"genre": "self-help", "icon": "bi-lightbulb"},
        {"genre": "adventure", "icon": "bi-compass"}
    ]

    return render(request, "reader/profile.html", {
        "books": mock_books,
        "genres": genres,
    })

def settings(request):
    return render(request, "reader/settings.html")


    