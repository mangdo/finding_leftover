# Generated by Django 3.1.2 on 2020-11-05 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='store', serialize=False, to='auth.user')),
                ('store_name', models.CharField(blank=True, max_length=50)),
                ('store_address', models.CharField(blank=True, max_length=50)),
                ('store_image', models.ImageField(default='default_image.jpg', upload_to='store')),
                ('store_memo', models.TextField(blank=True, null=True)),
                ('store_like', models.IntegerField(blank=True, null=True)),
                ('store_local', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
