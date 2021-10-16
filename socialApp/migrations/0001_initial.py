# Generated by Django 3.0.3 on 2021-10-12 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usersApp', '0002_auto_20211012_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='post_images')),
                ('normal_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersApp.NormalUser')),
            ],
        ),
    ]