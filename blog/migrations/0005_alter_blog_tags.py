# Generated by Django 5.1.3 on 2024-12-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_tag_blog_blog_tags_alter_blog_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='blog', to='blog.tag'),
        ),
    ]
