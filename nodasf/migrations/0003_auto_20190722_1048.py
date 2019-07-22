# Generated by Django 2.1.10 on 2019-07-22 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0002_auto_20190722_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='local_link',
            old_name='title',
            new_name='headline',
        ),
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media/stock'),
        ),
        migrations.AddField(
            model_name='city',
            name='imageQ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media/stock'),
        ),
        migrations.AddField(
            model_name='event',
            name='imageQ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='issue',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media/stock'),
        ),
        migrations.AddField(
            model_name='issue',
            name='imageQ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media/stock'),
        ),
        migrations.AddField(
            model_name='venue',
            name='imageQ',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='local_link',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.City'),
        ),
        migrations.AlterField(
            model_name='local_link',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media/stock'),
        ),
        migrations.AlterField(
            model_name='local_link',
            name='issue',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Issue'),
        ),
    ]
