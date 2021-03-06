# Generated by Django 3.1.5 on 2021-02-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WelcomeApp', '0011_auto_20210209_1831'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='imgresource',
            name='resourcePresent',
        ),
        migrations.AddConstraint(
            model_name='imgresource',
            constraint=models.CheckConstraint(check=models.Q(('link__isnull', True), ('resourceFile__isnull', True), _connector='OR'), name='resourcePresent'),
        ),
    ]
