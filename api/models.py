from django.db import models
from tinymce.models import HTMLField  # Import TinyMCE's HTMLField for rich text fields

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='technology/', blank=True, null=True)
    version = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (v{self.version})"

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"


class Framework(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name="frameworks")
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='framework/', blank=True, null=True)
    version = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (v{self.version})"

    class Meta:
        verbose_name = "Framework"
        verbose_name_plural = "Frameworks"


class Architecture(models.Model):
    flow_diagram = models.ImageField(upload_to='flow_diagram/', blank=True, null=True)
    system_architecture = models.FileField(upload_to='system_architecture/', blank=True, null=True)
    deployment_architecture = models.FileField(upload_to='deployment_architecture/', blank=True, null=True)
    dfd = models.FileField(upload_to='dfd/', blank=True, null=True)
    class_diagram = models.FileField(upload_to='class_diagram/', blank=True, null=True)
    wireframes = models.FileField(upload_to='wireframes/', blank=True, null=True)
    ui_design = models.FileField(upload_to='ui/', blank=True, null=True)

    def __str__(self):
        return "Architecture Details"

    class Meta:
        verbose_name = "Architecture"
        verbose_name_plural = "Architectures"


class Document(models.Model):
    installation_manual = models.FileField(upload_to='documents/', blank=True, null=True)
    user_manual = models.FileField(upload_to='documents/', blank=True, null=True)
    instructional_guide = models.FileField(upload_to='documents/', blank=True, null=True)
    tutorial = models.FileField(upload_to='tutorials/', blank=True, null=True)
    troubleshooting_guide = models.FileField(upload_to='documents/', blank=True, null=True)
    api_documentation = models.FileField(upload_to='documents/', blank=True, null=True)
    ux_documentation = models.FileField(upload_to='documents/', blank=True, null=True)
    testing_report = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return "Document Set"

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"


class Security(models.Model):
    security_standards = HTMLField()  # Use TinyMCE for rich text
    application_security = HTMLField()  # Use TinyMCE for rich text
    database_security = HTMLField()  # Use TinyMCE for rich text
    role = HTMLField()  # Use TinyMCE for rich text
    auditing = HTMLField()  # Use TinyMCE for rich text

    def __str__(self):
        return "Security Details"

    class Meta:
        verbose_name = "Security"
        verbose_name_plural = "Security Details"


class HardwareRequirement(models.Model):
    hardware_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    hardware_specification = models.TextField(blank=True)

    min_cpu = models.CharField(max_length=255)
    min_gpu = models.CharField(max_length=255, blank=True)
    min_ram = models.PositiveIntegerField()
    min_storage = models.PositiveIntegerField()
    min_network = models.CharField(max_length=255, blank=True)
    min_os = models.CharField(max_length=255)

    rec_cpu = models.CharField(max_length=255)
    rec_gpu = models.CharField(max_length=255, blank=True)
    rec_ram = models.PositiveIntegerField()
    rec_storage = models.PositiveIntegerField()
    rec_network = models.CharField(max_length=255, blank=True)
    rec_os = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SourceCode(models.Model):
    version_name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    description = HTMLField()  # Use TinyMCE for rich text
    source_code = models.FileField(upload_to='code/')

    def __str__(self):
        return f"{self.version_name} (v{self.version})"

    class Meta:
        verbose_name = "Source Code"
        verbose_name_plural = "Source Code Versions"


class Features(models.Model):
    feature_name = models.CharField(max_length=100)
    feature_description = HTMLField()  # Use TinyMCE for rich text

    def __str__(self):
        return f"{self.feature_name}-{self.feature_description}"


class FunctionalRequirement(models.Model):
    features = models.ManyToManyField(Features, related_name="functional_requirements")
    user_access_management = HTMLField()  # Use TinyMCE for rich text
    admin_panel = HTMLField()  # Use TinyMCE for rich text
    authentication_system = HTMLField()  # Use TinyMCE for rich text
    activity_log = HTMLField()  # Use TinyMCE for rich text
    backup = HTMLField()  # Use TinyMCE for rich text
    language = models.CharField(max_length=100)
    multiple_access = HTMLField()  # Use TinyMCE for rich text
    related_document_architecture = HTMLField()  # Use TinyMCE for rich text
    architecture = models.ForeignKey(Architecture, on_delete=models.CASCADE, related_name="functional_requirements")
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="functional_requirements")
    development_methodology = HTMLField()  # Use TinyMCE for rich text
    database = HTMLField()  # Use TinyMCE for rich text
    report_module = HTMLField()  # Use TinyMCE for rich text
    update_module = HTMLField()  # Use TinyMCE for rich text
    security = models.ForeignKey(Security, on_delete=models.CASCADE, related_name="functional_requirements")
    hardware_requirement = models.ForeignKey(HardwareRequirement, on_delete=models.CASCADE, related_name="functional_requirements")
    delivery_timelines = HTMLField()  # Use TinyMCE for rich text
    source_code = models.ManyToManyField(SourceCode, related_name="functional_requirements")
    platform = HTMLField()  # Use TinyMCE for rich text
    help_support = HTMLField()  # Use TinyMCE for rich text
    feedback = HTMLField()  # Use TinyMCE for rich text
    testing = HTMLField()  # Use TinyMCE for rich text
    training = HTMLField()  # Use TinyMCE for rich text
    warranty = HTMLField()  # Use TinyMCE for rich text
    operation_maintenance = HTMLField()  # Use TinyMCE for rich text

    def __str__(self):
        return self.feature_name

    class Meta:
        verbose_name = "Functional Requirement"
        verbose_name_plural = "Functional Requirements"


class NonFunctionalRequirement(models.Model):
    introduction = HTMLField()  # Use TinyMCE for rich text
    purpose = HTMLField()  # Use TinyMCE for rich text
    general_specifications = HTMLField()  # Use TinyMCE for rich text

    def __str__(self):
        return "Non-Functional Requirements"

    class Meta:
        verbose_name = "Non-Functional Requirement"
        verbose_name_plural = "Non-Functional Requirements"


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField()  # Use TinyMCE for rich text
    icon = models.ImageField(upload_to='project/', blank=True, null=True)
    technologies = models.ManyToManyField(Technology, related_name="projects")
    frameworks = models.ManyToManyField(Framework, related_name="projects")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="projects")
    functional_requirements = models.ManyToManyField(FunctionalRequirement, related_name="projects")
    nonfunctional_requirements = models.ManyToManyField(NonFunctionalRequirement, related_name="projects")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
