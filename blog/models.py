from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title',]

    def __str__(self):
        return self.title


class Post(models.Model):
    DRAFT = 'draft'
    ACTIVE = 'active'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField() # is not going to be the full body of the blog post but a short starter display
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-created_at',]



class Comment(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.message