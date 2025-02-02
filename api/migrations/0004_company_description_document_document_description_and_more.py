# Generated by Django 5.1.1 on 2025-01-31 23:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_features_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='document_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='features',
            name='feature_description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='activity_log',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='admin_panel',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='authentication_system',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='backup',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='database',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='delivery_timelines',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='development_methodology',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='feedback',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='help_support',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='multiple_access',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='operation_maintenance',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='platform',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='related_document_architecture',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='report_module',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='testing',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='training',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='update_module',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='user_access_management',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='functionalrequirement',
            name='warranty',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
