from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')

# api/v1/categories         GET
# api/v1/categories/1/      GET

# api/v1/courses            GET POST
# api/v1/courses/1/         GET DELETE

api.register(CourseResource())
api.register(CategoryResource())


urlpatterns = [
    path('', include(api.urls), name='index')
]
