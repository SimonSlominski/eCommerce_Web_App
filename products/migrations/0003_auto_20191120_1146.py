# Generated by Django 2.2.7 on 2019-11-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191120_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=21),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
