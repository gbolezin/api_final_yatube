from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.exceptions import BadRequest

from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer, GroupSerializer, FollowSerializer, PostSerializer
)
from posts.models import Follow, Group, Post

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_current_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))

    def get_queryset(self):
        post = self.get_current_post()
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_current_post()
        )


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.followed.all()

    def perform_create(self, serializer):
        following_user = User.objects.filter(
            username=self.request.data.get("following")).first()
        if not following_user:
            raise BadRequest('Отсутствует пользователь для подписки')
        follow = Follow.objects.filter(user=self.request.user,
                                       following=following_user).first()
        if follow:
            raise BadRequest('Подписка на пользователя '
                             f'{following_user.username} уже существует!')
        if following_user == self.request.user:
            raise BadRequest('Нельзя подписаться на самого себя!')
        serializer.save(
            user=self.request.user,
            following=following_user
        )
