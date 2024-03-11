from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    #path("", views.hello, name="hello"),
    path("style/home/", home_list_view, name="home"),
    path("<name>", views.hello_there, name="hello_there"),
    path("it_is/me", views.it_is_me, name="hello_it_is_me"),
    path("style/about/", views.about, name="about"),
    path("style/contact/", views.contact, name="contact"),
    #path("style/home/", views.my_home, name="my_home"),
    path("style/log/", views.log_message, name="log"),
    
]
