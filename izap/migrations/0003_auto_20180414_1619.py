# Generated by Django 2.0.4 on 2018-04-14 16:19

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('izap', '0002_auto_20180413_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='code',
        ),
        migrations.RemoveField(
            model_name='address',
            name='province',
        ),
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.CharField(default='00000-000', max_length=10, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='izap.City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='izap.State'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(default='BR', on_delete=django.db.models.deletion.PROTECT, to='izap.State', verbose_name='Estado'),
        ),
    ]
