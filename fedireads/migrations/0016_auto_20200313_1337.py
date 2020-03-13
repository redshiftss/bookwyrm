# Generated by Django 3.0.3 on 2020-03-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fedireads', '0015_auto_20200311_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('FAVORITE', 'Favorite'), ('REPLY', 'Reply'), ('TAG', 'Tag'), ('FOLLOW', 'Follow'), ('FOLLOW_REQUEST', 'Follow Request')], max_length=255),
        ),
        migrations.AddConstraint(
            model_name='notification',
            constraint=models.CheckConstraint(check=models.Q(notification_type__in=['FAVORITE', 'REPLY', 'TAG', 'FOLLOW', 'FOLLOW_REQUEST']), name='notification_type_valid'),
        ),
    ]
