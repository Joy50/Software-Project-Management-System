from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required(login_url='login')
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'dashboard.html', {'projects': projects})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.forms import formset_factory
from .forms import ProjectForm, NonFunctionalRequirementForm, FunctionalRequirementForm, ArchitectureForm, SecurityForm, SourceCodeForm, FeaturesForm, DocumentForm, HardwareRequirementForm

@login_required(login_url='login')
def create_project(request):
    # Formset factories with extra 1 form and can_delete set to True
    FeatureFormSet = formset_factory(FeaturesForm, extra=1, can_delete=True)
    DocumentFormSet = formset_factory(DocumentForm, extra=1, can_delete=True)
    HardwareRequirementFormSet = formset_factory(HardwareRequirementForm, extra=1, can_delete=True)

    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES)
        nonfunctional_requirement_form = NonFunctionalRequirementForm(request.POST)
        functionalrequirement_form = FunctionalRequirementForm(request.POST)
        architecture_form = ArchitectureForm(request.POST, request.FILES)
        security_form = SecurityForm(request.POST)
        source_code_form = SourceCodeForm(request.POST, request.FILES)

        # Initialize formsets with POST data
        feature_formset = FeatureFormSet(request.POST, prefix='features')
        document_formset = DocumentFormSet(request.POST, request.FILES, prefix='documents')
        hardware_requirement_formset = HardwareRequirementFormSet(request.POST, prefix='hardware')

        # Check if all forms and formsets are valid
        if (project_form.is_valid() and
            nonfunctional_requirement_form.is_valid() and
            functionalrequirement_form.is_valid() and
            architecture_form.is_valid() and
            security_form.is_valid() and
            source_code_form.is_valid() and
            feature_formset.is_valid() and
            document_formset.is_valid() and
            hardware_requirement_formset.is_valid()):

            try:
                with transaction.atomic():
                    # Save main project-related forms
                    project = project_form.save()
                    nonfunctional_requirement = nonfunctional_requirement_form.save()
                    functional_requirement = functionalrequirement_form.save()
                    architecture = architecture_form.save()
                    security = security_form.save()
                    source_code = source_code_form.save()

                    # Associate project-related forms with the project
                    project.nonfunctional_requirements.add(nonfunctional_requirement)
                    project.functional_requirements.add(functional_requirement)
                    project.architecture = architecture
                    project.security = security
                    project.source_code.add(source_code)

                    # Save feature formset
                    for feature_form in feature_formset:
                        if feature_form.cleaned_data and feature_form.is_valid():
                            feature = feature_form.save()
                            project.features.add(feature)

                    # Save document formset
                    for document_form in document_formset:
                        if document_form.cleaned_data and document_form.is_valid():
                            document = document_form.save()
                            project.documents.add(document)

                    # Save hardware requirement formset
                    for hardware_form in hardware_requirement_formset:
                        if hardware_form.cleaned_data and hardware_form.is_valid():
                            hardware = hardware_form.save()
                            project.hardware_requirements.add(hardware)

                    project.save()

                messages.success(request, "Project created successfully.")
                return redirect('dashboard')

            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('create_project')

        else:
            # If any form is invalid, show the form errors
            messages.error(request, "Please correct the errors in the form.")
            print("Project Form Errors:", project_form.errors)
            print("Non-functional Requirement Form Errors:", nonfunctional_requirement_form.errors)
            print("Functional Requirement Form Errors:", functionalrequirement_form.errors)
            print("Architecture Form Errors:", architecture_form.errors)
            print("Security Form Errors:", security_form.errors)
            print("Source Code Form Errors:", source_code_form.errors)
            print("Feature Formset Errors:", feature_formset.errors)
            print("Document Formset Errors:", document_formset.errors)
            print("Hardware Requirement Formset Errors:", hardware_requirement_formset.errors)

    else:
        # Initialize empty forms and formsets for GET request
        project_form = ProjectForm()
        nonfunctional_requirement_form = NonFunctionalRequirementForm()
        functionalrequirement_form = FunctionalRequirementForm()
        architecture_form = ArchitectureForm()
        security_form = SecurityForm()
        source_code_form = SourceCodeForm()

        feature_formset = FeatureFormSet(prefix='features')
        document_formset = DocumentFormSet(prefix='documents')
        hardware_requirement_formset = HardwareRequirementFormSet(prefix='hardware')

    return render(request, 'project_form.html', {
        'project_form': project_form,
        'nonfunctional_requirement_form': nonfunctional_requirement_form,
        'functionalrequirement_form': functionalrequirement_form,
        'architecture_form': architecture_form,
        'security_form': security_form,
        'source_code_form': source_code_form,
        'feature_formset': feature_formset,
        'document_formset': document_formset,
        'hardware_requirement_formset': hardware_requirement_formset,
    })


@login_required(login_url='login')
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        "project": project,
        "features": project.features.all(),
        "documents": project.documents.all(),
        "architecture": project.architecture,
        "security": project.security,
        "hardware_requirements": project.hardware_requirements.all(),
        "source_code": project.source_code.all(),
        "technologies": project.technologies.all(),
        "frameworks": project.frameworks.all(),
    }
    return render(request, "project_detail.html", context)

@login_required(login_url='login')
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES, instance=project)
        functional_form = FunctionalRequirementForm(request.POST, instance=project.functional_requirements.first())
        nonfunctional_form = NonFunctionalRequirementForm(request.POST, instance=project.nonfunctional_requirements.first())
        architecture_form = ArchitectureForm(request.POST, request.FILES, instance=project.architecture)
        document_form = DocumentForm(request.POST, request.FILES, instance=project.documents.first())  # Assuming one document per project
        security_form = SecurityForm(request.POST, instance=project.security)
        hardware_form = HardwareRequirementForm(request.POST, instance=project.hardware_requirements.first())  # Assuming one hardware requirement
        source_code_form = SourceCodeForm(request.POST, request.FILES)

        if (project_form.is_valid() and functional_form.is_valid() and 
            nonfunctional_form.is_valid() and architecture_form.is_valid() and 
            document_form.is_valid() and security_form.is_valid() and 
            hardware_form.is_valid() and source_code_form.is_valid()):

            project_form.save()
            functional_form.save()
            nonfunctional_form.save()
            architecture_form.save()
            document_form.save()
            security_form.save()
            hardware_form.save()

            # Save new source code version
            source_code = source_code_form.save(commit=False)
            source_code.project = project
            source_code.save()

            messages.success(request, "Project updated successfully.")
            return redirect('project_detail', project_id=project.id)

    else:
        project_form = ProjectForm(instance=project)
        functional_form = FunctionalRequirementForm(instance=project.functional_requirements.first())
        nonfunctional_form = NonFunctionalRequirementForm(instance=project.nonfunctional_requirements.first())
        architecture_form = ArchitectureForm(instance=project.architecture)
        document_form = DocumentForm(instance=project.documents.first())
        security_form = SecurityForm(instance=project.security)
        hardware_form = HardwareRequirementForm(instance=project.hardware_requirements.first())
        source_code_form = SourceCodeForm()

    return render(request, "edit_project.html", {
        "project_form": project_form,
        "functional_form": functional_form,
        "nonfunctional_form": nonfunctional_form,
        "architecture_form": architecture_form,
        "document_form": document_form,
        "security_form": security_form,
        "hardware_form": hardware_form,
        "source_code_form": source_code_form,
        "project": project,
    })

@login_required(login_url='login')
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect("dashboard")

    return render(request, "delete_project.html", {"project": project})

@login_required(login_url='login')
def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Company added successfully!")
            return redirect("dashboard")
    else:
        form = CompanyForm()
    
    return render(request, "form.html", {"form": form, "title":"Company"})

@login_required(login_url='login')
def add_technology(request):
    if request.method == "POST":
        form = TechnologyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Technology added successfully!")
            return redirect("dashboard")
    else:
        form = TechnologyForm()
    
    return render(request, "form.html", {"form": form, "title":"Technology"})

@login_required(login_url='login')
def add_framework(request):
    if request.method == "POST":
        form = FrameworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Framework added successfully!")
            return redirect("dashboard")
    else:
        form = FrameworkForm()
    
    return render(request, "form.html", {"form": form, "title":"Framework"})
