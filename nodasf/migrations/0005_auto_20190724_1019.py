# Generated by Django 2.1.10 on 2019-07-24 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0004_city_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ('name',)},
        ),
    ]
