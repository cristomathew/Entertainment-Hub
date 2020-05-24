# Generated by Django 3.0.4 on 2020-05-24 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sub_categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='videos/{{category}}/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_categories.SubCategory')),
            ],
        ),
    ]
