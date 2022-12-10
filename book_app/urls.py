from django.urls import path, include
from graphene_django.views import GraphQLView
from book_app.schema import schema


urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
