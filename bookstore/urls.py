from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^user/',include('users.urls',namespace='user')),#用户模块
    url(r'^tinymce/',include('tinymce.urls')),#富文本编辑器
    url(r'^',include('books.urls',namespace='index')),#商品模块首页
    url(r'^books/',include('books.urls',namespace='books')),#商品模块
    ]




