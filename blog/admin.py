from django.contrib import admin
from .models import Article,Category

#custome code for admin pannel djang

admin.site.site_header = "پنل مدیریت سایت"

# Register your models here.
@admin.action(description="منتشر کردن موارد انتخاب شده")
def make_published(modeladmin, request, queryset):
    queryset.update(status="P") # Update status to p

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','published','thumpnail_tag','category_to_str')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('title', 'description')
    actions = [make_published]
    # sakhte shodan slug bad asase title
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created',)

    #many to many field ro nemishe namayash dad to admin o va bayad be sorate dasti gerft va be str tabdil kard
    def category_to_str(self,obj):
        return ",".join([category.title for category in obj.category_publish()])
    category_to_str.short_description = "دسته بندی"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title', 'slug', 'status','parent')
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}

