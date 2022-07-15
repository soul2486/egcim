from django.urls import path, include, re_path


from django.contrib import admin

admin.autodiscover()

urlpatterns =[
                path('admin/', admin.site.urls),
                path('plag/', include('plag.urls')),
]
