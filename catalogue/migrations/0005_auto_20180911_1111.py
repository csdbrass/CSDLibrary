# Generated by Django 2.1 on 2018-09-11 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20180911_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='arranger',
            field=models.ManyToManyField(help_text='Select one or more names', related_name='arranger', to='catalogue.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='died',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='piece',
            name='feature',
            field=models.ManyToManyField(help_text='Select one or more instruments', to='catalogue.Instrument'),
        ),
        migrations.AddField(
            model_name='piece',
            name='genre',
            field=models.ForeignKey(blank=True, help_text='Select one genre', null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogue.Genre'),
        ),
    ]
