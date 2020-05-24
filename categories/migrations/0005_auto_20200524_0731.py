# Generated by Django 3.0.4 on 2020-05-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='typ',
            field=models.CharField(choices=[('Drama', 'Drama'), ('Action', 'Action'), ('Comedy', 'Comedy')], default='Comedy', max_length=100),
        ),
    ]
