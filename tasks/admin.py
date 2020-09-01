from django.contrib import admin

from tasks.models import TodoItem, Category


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'is_completed', 'created')

    def category(self, instance):
        return instance.category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')



