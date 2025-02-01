from django.contrib import admin
from django import forms
from .models import Project, Company, Technology, Framework, Architecture, Document, Security, HardwareRequirement, SourceCode, Features, FunctionalRequirement, NonFunctionalRequirement


# Inline admin formsets for related models

class TechnologyInline(admin.TabularInline):
    model = Project.technologies.through  # Many-to-many relationship with Technology
    extra = 1
    can_delete = True


class FrameworkInline(admin.TabularInline):
    model = Project.frameworks.through  # Many-to-many relationship with Framework
    extra = 1
    can_delete = True


class FunctionalRequirementInline(admin.TabularInline):
    model = Project.functional_requirements.through  # Many-to-many relationship with FunctionalRequirement
    extra = 1
    can_delete = True


class NonFunctionalRequirementInline(admin.TabularInline):
    model = Project.nonfunctional_requirements.through  # Many-to-many relationship with NonFunctionalRequirement
    extra = 1
    can_delete = True


# Custom form for ProjectAdmin if necessary
class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Add any custom validation logic here if needed
        return cleaned_data


# Main ProjectAdmin
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    # Specify inlines for related models
    inlines = [TechnologyInline, FrameworkInline, FunctionalRequirementInline, NonFunctionalRequirementInline]

    # List view settings
    list_display = ('name', 'company', 'description')
    search_fields = ('name', 'company__name')
    list_filter = ('company',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # You can add custom save logic if necessary

    # You can customize more properties as needed

# Registering the models with their admin configurations
admin.site.register(Project, ProjectAdmin)
admin.site.register(Company)
admin.site.register(Technology)
admin.site.register(Framework)
admin.site.register(Architecture)
admin.site.register(Document)
admin.site.register(Security)
admin.site.register(HardwareRequirement)
admin.site.register(SourceCode)
admin.site.register(Features)
admin.site.register(FunctionalRequirement)
admin.site.register(NonFunctionalRequirement)
