# Generated by Django 3.2.5 on 2021-07-13 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerGuide', '0002_alter_flower_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='flowerSlug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flower',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
