# Generated by Django 3.2.18 on 2023-04-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='班级')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=32, verbose_name='时间')),
                ('tuesday', models.CharField(max_length=128, verbose_name='周二')),
                ('monday', models.CharField(max_length=128, verbose_name='周一')),
                ('wednesday', models.CharField(max_length=128, verbose_name='周三')),
                ('thursday', models.CharField(max_length=128, verbose_name='周四')),
                ('friday', models.CharField(max_length=128, verbose_name='周五')),
                ('sunday', models.CharField(max_length=128, verbose_name='周六')),
                ('saturday', models.CharField(max_length=128, verbose_name='周日')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, verbose_name='学号')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('phone_number', models.CharField(max_length=64, verbose_name='联系电话')),
                ('dormitory_number', models.CharField(max_length=64, verbose_name='宿舍编号')),
            ],
        ),
    ]