from django.urls import path

from sitepage.views import HomePageView, DonatePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('donate/', DonatePageView.as_view(), name='donate'),
]