from django.db import models


class Post(models.Model):
    """Post Model

    This is the model that represents an instance of a blog post.
    """
    title = models.CharField(max_length=200)
    author
    status
    created_date
    published_date
    body
