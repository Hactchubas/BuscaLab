# Generated by Django 3.2.19 on 2023-06-03 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busca_lab', '0010_rename_qauntity_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='quantity',
            options={'ordering': ['-lab']},
        ),
        migrations.AddField(
            model_name='lab',
            name='equipaments',
            field=models.ManyToManyField(blank=True, related_name='are_in', to='busca_lab.Equipament'),
        ),
    ]
