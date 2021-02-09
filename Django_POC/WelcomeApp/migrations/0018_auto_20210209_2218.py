# Generated by Django 3.1.5 on 2021-02-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WelcomeApp', '0017_auto_20210209_2213'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='imgresource',
            name='resourcePresent',
        ),
        migrations.AddConstraint(
            model_name='imgresource',
            constraint=models.CheckConstraint(check=models.Q(('link__exact', ''), ('resourceFile__exact', ''), _negated=True), name='resourcePresent'),
        ),
    ]
