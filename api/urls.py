from django.urls import path
from .views import (
    dashboard,
    create_project,
    project_detail,
    edit_project,
    delete_project,
    add_company,
    add_technology,
    add_framework,
)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    
    # Project-related URLs
    path("project/create/", create_project, name="create_project"),
    path("project/<int:project_id>/", project_detail, name="project_detail"),
    path("project/<int:project_id>/edit/", edit_project, name="edit_project"),
    path("project/<int:project_id>/delete/", delete_project, name="delete_project"),

    # Company, Technology, and Framework URLs
    path("company/add/", add_company, name="add_company"),
    path("technology/add/", add_technology, name="add_technology"),
    path("framework/add/", add_framework, name="add_framework"),
]
