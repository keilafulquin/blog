# Generated by Django 4.1.1 on 2022-11-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img-publicaciones'),
        ),
        migrations.DeleteModel(
            name='Imagenes',
        ),
    ]
