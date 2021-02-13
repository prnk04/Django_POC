# Generated by Django 3.1.5 on 2021-02-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WelcomeApp', '0019_auto_20210209_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=500)),
                ('dateSubmitted', models.DateField(auto_now_add=True)),
                ('link', models.URLField(blank=True)),
                ('resourceFile', models.FileField(blank=True, upload_to='videoResources')),
            ],
        ),
        migrations.AddConstraint(
            model_name='videoresource',
            constraint=models.UniqueConstraint(fields=('resource_name', 'authors'), name='unique_videoResources'),
        ),
        migrations.AddConstraint(
            model_name='videoresource',
            constraint=models.CheckConstraint(check=models.Q(('link__exact', ''), ('resourceFile__exact', ''), _negated=True), name='videoPresent'),
        ),
    ]