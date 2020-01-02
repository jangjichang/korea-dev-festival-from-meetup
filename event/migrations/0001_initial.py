# Generated by Django 2.2 on 2020-01-02 02:47

from django.db import migrations, models
import django.db.models.deletion
import meetupcrawler.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WaitingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='facebook_crawling', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='UserrequestEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='user_request', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='NotDevEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='user_request', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='MeetupCrawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='meetup_crawling', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='ManualEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='manual', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='FestaCrawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='festa_crawling', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='FacebookCrawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='facebook_crawling', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='EventusCrawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='eventus_crawling', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='DevEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=meetupcrawler.utils.uuid_name_upload_to)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', 'manual'), ('user', 'user_request'), ('festa', 'festa_crawling'), ('meetup', 'meetup_crawling'), ('eventus', 'eventus_crawling'), ('facebook', 'facebook_crawling')], default='user_request', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
    ]
