from django.urls import path

from .views import NoticeSettingsView

app_name = "pinax_notifications"

urlpatterns = [
    re_path(r"^settings/$", NoticeSettingsView.as_view(), name="notice_settings"),
]
