from django.urls import path
from .views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),  # Link the HomePageView to the root URL
]
