# Generated by Django 3.2 on 2021-04-20 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0006_auto_20210411_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date_added',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Tag',
            new_name='tags',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]