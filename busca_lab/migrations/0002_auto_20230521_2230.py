# Generated by Django 3.2.19 on 2023-05-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busca_lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PC_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('processor', models.CharField(max_length=255)),
                ('cpu_mark', models.IntegerField()),
                ('mem_capacity', models.CharField(max_length=6)),
                ('mem_type', models.CharField(max_length=64)),
                ('operational_system', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('lisence', models.CharField(max_length=64)),
                ('version', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='lab',
            name='pc_models',
            field=models.ManyToManyField(blank=True, related_name='locals', to='busca_lab.PC_model'),
        ),
        migrations.AddField(
            model_name='lab',
            name='softwares',
            field=models.ManyToManyField(blank=True, related_name='installed_in', to='busca_lab.Software'),
        ),
    ]
