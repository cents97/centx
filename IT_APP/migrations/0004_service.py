# Generated by Django 3.2.25 on 2025-03-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_APP', '0003_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/')),
                ('link', models.CharField(default='/contact/', help_text='URL for the service button', max_length=255)),
            ],
        ),
    ]
