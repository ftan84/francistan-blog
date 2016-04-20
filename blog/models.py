from django.db import models


class Author(models.Model):
    """Author Model

    Model that represents an instance of the author.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Post(models.Model):
    """Post Model

    This is the model that represents an instance of a blog post.
    """
    STATUS_CHOICES = (
        ('private', 'Private'),
        ('public', 'Public')
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    status = models.CharField(max_length=200,
                              choices=STATUS_CHOICES,
                              default='private')
    created = models.DateTimeField('date created')
    published = models.DateTimeField('date published')
    body = models.TextField()
