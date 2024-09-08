from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', )
    search_fields = ('name', )
    ordering = ('name', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'movie', )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)

