# Generated by Django 4.1.7 on 2023-03-20 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_section_images_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='images',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='section_images')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='base.section')),
            ],
        ),
    ]
