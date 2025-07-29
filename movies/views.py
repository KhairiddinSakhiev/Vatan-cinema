from django.shortcuts import render
from django.db.models import Q
from .models import Movie, MovieCategory, Trailer
from tickets.models import Show

def home_view(request):
    movies = Movie.objects.filter(is_active=True)
    search_query = request.GET.get('search')
    if search_query:
        movies = movies.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    category_id = request.GET.get('category')
    if category_id:
        movies = movies.filter(category_id=category_id)

    year = request.GET.get('year')
    if year:
        movies = movies.filter(rel_year=year)

    trailers = Trailer.objects.filter(is_active=True).order_by('-created_at')[:5]
    categories = MovieCategory.objects.all()
    shows = Show.objects.all()

    context = {
        "trailers": trailers,      
        "movies": movies,          
        "categories": categories,  
        "shows": shows,           
    }
    return render(request, "home.html", context)
