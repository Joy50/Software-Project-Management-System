# Generated by Django 5.1.1 on 2025-01-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functionalrequirement',
            name='project',
        ),
        migrations.RemoveField(
            model_name='nonfunctionalrequirement',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='frameworks',
            field=models.ManyToManyField(related_name='projects', to='api.framework'),
        ),
        migrations.AddField(
            model_name='project',
            name='functional_requirements',
            field=models.ManyToManyField(related_name='projects', to='api.functionalrequirement'),
        ),
        migrations.AddField(
            model_name='project',
            name='nonfunctional_requirements',
            field=models.ManyToManyField(related_name='projects', to='api.nonfunctionalrequirement'),
        ),
    ]
