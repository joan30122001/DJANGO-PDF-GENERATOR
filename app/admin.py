from django.contrib import admin
from . models import Title, SubTitle, Template, Cover, BoardTitle, BoardElement, ChartImage



admin.site.register(Title)
admin.site.register(Cover)
admin.site.register(Template)
admin.site.register(SubTitle)
admin.site.register(BoardTitle)
admin.site.register(BoardElement)
admin.site.register(ChartImage)