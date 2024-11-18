from django.contrib import admin
from .models import Post, Comment, Category


class CommentItemInline(admin.TabularInline): # To display comments in the post 
    model = Comment
    row_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','intro','body']
    list_display = ['title','slug','category','created_at','status']
    list_filter = ['category', 'created_at','status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug' : ('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title','slug']
    list_display = ['title','slug']
    prepopulated_fields = {'slug' : ('title',)} # Auto-generate the slug
    
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','post','comment','email','created_at']
    list_filter = ['name', 'created_at']

    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
