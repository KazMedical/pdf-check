from django.contrib import admin
from django.urls import path
from pdfrender.views import generate_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pdf-render/", generate_pdf, name="pdf-render"),
]
