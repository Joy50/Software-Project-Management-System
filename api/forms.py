from django import forms
from .models import *

class BootstrapMixin(forms.ModelForm):
    """A mixin to add Bootstrap classes to form fields dynamically."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widget_classes = {
            forms.Textarea: {'class': 'form-control', 'rows': 3},
            forms.Select: {'class': 'form-control'},
            forms.CheckboxSelectMultiple: {'class': 'form-check'},
            forms.CheckboxInput: {'class': 'form-check-input'},
            forms.FileInput: {'class': 'form-control'},  # Bootstrap 5+ uses 'form-control' for file inputs
        }

        for field_name, field in self.fields.items():
            widget_type = type(field.widget)
            if widget_type in widget_classes:
                field.widget.attrs.update(widget_classes[widget_type])
            else:
                field.widget.attrs.update({'class': 'form-control'})  # Default Bootstrap styling

class CompanyForm(BootstrapMixin):
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone', 'email', 'website']

class TechnologyForm(BootstrapMixin):
    class Meta:
        model = Technology
        fields = ['name', 'icon', 'version']

class FrameworkForm(BootstrapMixin):
    class Meta:
        model = Framework
        fields = ['technology', 'name', 'icon', 'version']

class ArchitectureForm(BootstrapMixin):
    class Meta:
        model = Architecture
        fields = ['flow_diagram', 'system_architecture', 'dfd', 'class_diagram', 'wireframes', 'ui_design']

class DocumentForm(BootstrapMixin):
    class Meta:
        model = Document
        fields = [
            'installation_manual', 'user_manual', 'instructional_guide', 'tutorial',
            'troubleshooting_guide', 'api_documentation', 'ux_documentation', 'testing_report'
        ]

class SecurityForm(BootstrapMixin):
    class Meta:
        model = Security
        fields = ['security_standards', 'application_security', 'database_security', 'role', 'auditing']
        widgets = {field: forms.Textarea(attrs={'rows': 3}) for field in fields}  # Auto-apply Textarea rows

class HardwareRequirementForm(BootstrapMixin):
    class Meta:
        model = HardwareRequirement
        fields = [
            'hardware_name', 'brand', 'hardware_specification', 'min_cpu', 'min_gpu',
            'min_ram', 'min_storage', 'min_network', 'min_os', 'rec_cpu', 'rec_gpu',
            'rec_ram', 'rec_storage', 'rec_network', 'rec_os'
        ]
        widgets = {'hardware_specification': forms.Textarea(attrs={'rows': 3})}

class SourceCodeForm(BootstrapMixin):
    class Meta:
        model = SourceCode
        fields = ['version_name', 'version', 'description', 'source_code']
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}

class FeaturesForm(BootstrapMixin):
    class Meta:
        model = Features
        fields = ['feature_name', 'feature_description']
        widgets = {'feature_description': forms.Textarea(attrs={'rows': 3})}

class FunctionalRequirementForm(BootstrapMixin):
    class Meta:
        model = FunctionalRequirement
        fields = [
            'user_access_management', 'admin_panel', 'authentication_system', 'activity_log',
            'backup', 'language', 'multiple_access', 'related_document_architecture',
            'development_methodology', 'database', 'report_module', 'update_module'
        ]
        widgets = {field: forms.Textarea(attrs={'rows': 3}) for field in fields if field != 'language'}

class NonFunctionalRequirementForm(BootstrapMixin):
    class Meta:
        model = NonFunctionalRequirement
        fields = ['introduction', 'purpose', 'general_specifications']
        widgets = {field: forms.Textarea(attrs={'rows': 3}) for field in fields}

class ProjectForm(BootstrapMixin):
    class Meta:
        model = Project
        fields = ['name', 'description', 'icon', 'technologies', 'frameworks', 'company']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'technologies': forms.CheckboxSelectMultiple(),
            'frameworks': forms.CheckboxSelectMultiple(),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }
