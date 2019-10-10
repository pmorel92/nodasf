# Generated by Django 2.2.4 on 2019-10-10 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0023_auto_20190904_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stf',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.City'),
        ),
        migrations.AlterField(
            model_name='stf',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.County'),
        ),
        migrations.AlterField(
            model_name='stf',
            name='hub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodasf.STF_Hub'),
        ),
        migrations.AlterField(
            model_name='stf',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Issue'),
        ),
        migrations.AlterField(
            model_name='stf_hub',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.City'),
        ),
        migrations.AlterField(
            model_name='stf_hub',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.County'),
        ),
        migrations.AlterField(
            model_name='stf_hub',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Issue'),
        ),
    ]
