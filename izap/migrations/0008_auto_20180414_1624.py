# Generated by Django 2.0.4 on 2018-04-14 16:24

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('izap', '0007_auto_20180414_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='izap.City', verbose_name='cidade'),
        ),
    ]
