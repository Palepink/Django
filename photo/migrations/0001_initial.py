# Generated by Django 2.0.7 on 2018-08-07 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('slug', models.SlugField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('photo', models.ImageField(upload_to='images/%Y%m%d')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
