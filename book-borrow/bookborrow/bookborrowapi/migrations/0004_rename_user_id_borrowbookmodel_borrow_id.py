# Generated by Django 5.0.3 on 2024-03-26 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookborrowapi', '0003_alter_borrowbookmodel_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowbookmodel',
            old_name='user_id',
            new_name='borrow_id',
        ),
    ]
