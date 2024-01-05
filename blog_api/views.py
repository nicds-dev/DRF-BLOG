from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import permissions

class PostUserWritePermission(permissions.BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.id == request.user.id
        

class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer