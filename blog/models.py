from django.db import models


class Author(models.Model):
    """Author Model

    Model that represents an instance of the author.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

class Post(models.Model):
    """Post Model

    This is the model that represents an instance of a blog post.
    """
    STATUS_CHOICES = (
        ('private', 'Private'),
        ('public', 'Public')
    )
    title = models.CharField(max_length=200)
    # slug = models.SlugField(unique=True)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    status = models.CharField(max_length=200,
                              choices=STATUS_CHOICES,
                              default='private')
    created = models.DateTimeField('date created', auto_now_add=True)
    published = models.DateTimeField('date published', null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
