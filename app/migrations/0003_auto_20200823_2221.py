# Generated by Django 3.0.6 on 2020-08-24 03:21

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200823_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='department',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='country', chained_model_field='country', default='', on_delete=django.db.models.deletion.CASCADE, to='app.Department'),
        ),
    ]
