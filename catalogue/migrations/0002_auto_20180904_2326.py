# Generated by Django 2.1 on 2018-09-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, help_text="Enter individual's personal name", max_length=200)),
                ('surname', models.CharField(help_text="Enter individual's family name", max_length=200)),
            ],
            options={
                'ordering': ['surname', 'firstName'],
            },
        ),
        migrations.AlterField(
            model_name='piece',
            name='note',
            field=models.TextField(blank=True, help_text='Enter any noteworthy information about the piece', max_length=1000),
        ),
        migrations.AddField(
            model_name='piece',
            name='composer',
            field=models.ManyToManyField(to='catalogue.Person'),
        ),
    ]
