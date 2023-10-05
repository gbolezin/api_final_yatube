class CreateFollowMixin():
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )


class ListFollowMixin():
    def get_queryset(self):
        return self.request.user.follower.all()
