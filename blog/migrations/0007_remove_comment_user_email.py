# Generated by Django 5.0.3 on 2024-04-25 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_text_alter_comment_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_email',
        ),
    ]
