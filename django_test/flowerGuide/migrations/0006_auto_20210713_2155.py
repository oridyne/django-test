# Generated by Django 3.2.5 on 2021-07-14 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowerGuide', '0005_alter_flower_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='FlowerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowerGuide.flower')),
            ],
        ),
    ]
