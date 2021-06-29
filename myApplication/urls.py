from django.urls import path, re_path
from myApplication import views

urlpatterns = [
    # 普通字符串模式
    # 什么都不写 ：127.0.0.1:8080
    # path('', views.index),
    # path('t1', views.test)

    # 正则表达式模式
    # re_path('^$', views.index),
    # re_path('^t1$', views.test)

    # 路由的规则是：只要有符合的 下面的就不会走了
    path('articles/2021/', views.special_case_2021),
    # 用这种方式写的，<>里面的参数会当做形参传到year_archive函数中
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
