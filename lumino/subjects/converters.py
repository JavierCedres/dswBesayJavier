from django.shortcuts import get_object_or_404


class PostConverter:
    regex = r'[\w-]+'

    def to_python(self, post_slug: str) -> Subject:
        return get_object_or_404(Subject, slug=post_slug)

    def to_url(self, post: Subject) -> str:
        return post.slug
