from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):
    ACTIVE = 'active' # Value will store in database
    DRAFT = 'draft'   # Value will store in database  

    CHOICES_STATUS = (
        (ACTIVE, 'Active'), # Value will see in admin interface
        (DRAFT, 'Draft')    # Value will see in admin interface
        )

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    intro = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(User, default='admin', on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads',blank=True, null=True)    
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created_at',)
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug,self.slug)    

# Comment Models
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        return f"Comment posted by {self.name} on {self.post.title}"