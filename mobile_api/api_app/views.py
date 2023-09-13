from django.forms import model_to_dict
from rest_framework import generics,permissions,pagination
from .models import Posts
from .Serializers import PostsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PostAPIListPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 10000


class PostApiview(generics.ListAPIView):
    """Показывает посты, принимает limit для указания количества"""
    queryset = Posts.objects.all()
    pagination_class = PostAPIListPagination
    serializer_class = PostsSerializer


class PostApiviewDelete(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAdminUser, ]

class GetCreateUserPosts(APIView):
    """Добавление и просмотр постов пользователем авторизованным через токен"""
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, format=None):
        content = {
            'user': str(request.user.id),  # `django.contrib.auth.User` instance.
        }
        queryset = Posts.objects.all().filter(username=content['user']).values()
        return Response({'posts':list(queryset)})
    def post(self,request):
        post_new=Posts.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            username=request.user
        )
        return Response({'post':model_to_dict(post_new)})