from django.contrib import admin
from .models import LibraryUser, ReadingList, BookReview

admin.site.register(LibraryUser)
admin.site.register(ReadingList)
admin.site.register(BookReview)