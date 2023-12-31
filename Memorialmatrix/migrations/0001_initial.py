# Generated by Django 3.2 on 2022-12-07 18:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('type', models.CharField(blank=True, max_length=75, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=5, null=True)),
                ('time_active_start', models.DateField(blank=True, null=True)),
                ('time_active_end', models.DateField(blank=True, null=True)),
                ('lat_coord', models.DecimalField(blank=True, decimal_places=15, max_digits=17, null=True)),
                ('long_coord', models.DecimalField(blank=True, decimal_places=15, max_digits=18, null=True)),
                ('permanent', models.CharField(blank=True, choices=[('temporary', 'Temporary'), ('permanent', 'Permanent')], max_length=9, null=True)),
                ('location_approval', models.BooleanField(default=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('org_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('name', models.CharField(max_length=75)),
                ('primary_contact_name', models.CharField(max_length=75)),
                ('website', models.URLField(max_length=150)),
                ('type', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=500)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('webuser_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('web_user_loss', models.BooleanField(default=False)),
                ('email_updates', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('admin_number', models.IntegerField(default=1, editable=False)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='email address')),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zipcode', models.CharField(blank=True, max_length=5, validators=[django.core.validators.validate_integer, django.core.validators.MinLengthValidator(5)])),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_superuser', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
            },
        ),
        migrations.CreateModel(
            name='Memorial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('memorial_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('name', models.CharField(max_length=75)),
                ('type', models.CharField(blank=True, choices=[('physical', 'Physical'), ('virtual', 'Virtual')], max_length=75, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('google_virtual_tour', models.URLField(blank=True, null=True)),
                ('memorial_type_desc', models.CharField(blank=True, max_length=75, null=True)),
                ('founder_name', models.CharField(blank=True, max_length=75, null=True)),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('confirm_data_accuracy', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=4096, null=True)),
                ('social_media_twitter', models.URLField(blank=True, null=True)),
                ('social_media_facebook', models.URLField(blank=True, null=True)),
                ('social_media_instagram', models.URLField(blank=True, null=True)),
                ('is_approved', models.CharField(choices=[('pending', 'Pending'), ('disapproved', 'Disapproved'), ('approved', 'Approved')], default='Pending', max_length=11)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('mem_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mem_location', to='Memorialmatrix.location')),
                ('mem_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mem_organization', to='Memorialmatrix.organization')),
                ('mem_submitter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mem_submitter', to='Memorialmatrix.webuser')),
            ],
        ),
        migrations.CreateModel(
            name='MediaLinks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('medialinks_number', models.IntegerField(default=1, editable=False)),
                ('type', models.CharField(choices=[('photo', 'Photo'), ('video', 'Video'), ('press coverage', 'Press Coverage')], max_length=75)),
                ('url', models.URLField()),
                ('medialinks_approval', models.BooleanField(default=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('mem_medialinks', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mem_medialinks', to='Memorialmatrix.memorial')),
            ],
            options={
                'verbose_name': 'MediaLinks',
                'verbose_name_plural': 'MediaLinks',
            },
        ),
        migrations.CreateModel(
            name='History_WebUser',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('webuser_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('web_user_loss', models.BooleanField(default=False)),
                ('email_updates', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' History_WebUser',
                'db_table': 'History_WebUser',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='History_Organization',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('org_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('name', models.CharField(max_length=75)),
                ('primary_contact_name', models.CharField(max_length=75)),
                ('website', models.URLField(max_length=150)),
                ('type', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=500)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' History_Organization',
                'db_table': 'History_Organization',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='History_Memorial',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('memorial_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('name', models.CharField(max_length=75)),
                ('type', models.CharField(blank=True, choices=[('physical', 'Physical'), ('virtual', 'Virtual')], max_length=75, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('google_virtual_tour', models.URLField(blank=True, null=True)),
                ('memorial_type_desc', models.CharField(blank=True, max_length=75, null=True)),
                ('founder_name', models.CharField(blank=True, max_length=75, null=True)),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('confirm_data_accuracy', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=4096, null=True)),
                ('social_media_twitter', models.URLField(blank=True, null=True)),
                ('social_media_facebook', models.URLField(blank=True, null=True)),
                ('social_media_instagram', models.URLField(blank=True, null=True)),
                ('is_approved', models.CharField(choices=[('pending', 'Pending'), ('disapproved', 'Disapproved'), ('approved', 'Approved')], default='Pending', max_length=11)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('mem_location', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Memorialmatrix.location')),
                ('mem_organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Memorialmatrix.organization')),
                ('mem_submitter', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Memorialmatrix.webuser')),
            ],
            options={
                'verbose_name': ' History_Memorial',
                'db_table': 'History_Memorial',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='History_MediaLinks',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('medialinks_number', models.IntegerField(default=1, editable=False)),
                ('type', models.CharField(choices=[('photo', 'Photo'), ('video', 'Video'), ('press coverage', 'Press Coverage')], max_length=75)),
                ('url', models.URLField()),
                ('medialinks_approval', models.BooleanField(default=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('mem_medialinks', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Memorialmatrix.memorial')),
            ],
            options={
                'verbose_name': ' History_MediaLink',
                'db_table': 'History_MediaLinks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='History_Location',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('location_number', models.IntegerField(blank=True, default=1, editable=False)),
                ('type', models.CharField(blank=True, max_length=75, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=5, null=True)),
                ('time_active_start', models.DateField(blank=True, null=True)),
                ('time_active_end', models.DateField(blank=True, null=True)),
                ('lat_coord', models.DecimalField(blank=True, decimal_places=15, max_digits=17, null=True)),
                ('long_coord', models.DecimalField(blank=True, decimal_places=15, max_digits=18, null=True)),
                ('permanent', models.CharField(blank=True, choices=[('temporary', 'Temporary'), ('permanent', 'Permanent')], max_length=9, null=True)),
                ('location_approval', models.BooleanField(default=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' History_Location',
                'db_table': 'History_Location',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='History_Admin',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('admin_number', models.IntegerField(default=1, editable=False)),
                ('email', models.EmailField(db_index=True, max_length=254, validators=[django.core.validators.EmailValidator()], verbose_name='email address')),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zipcode', models.CharField(blank=True, max_length=5, validators=[django.core.validators.validate_integer, django.core.validators.MinLengthValidator(5)])),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_superuser', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' History_Admin',
                'db_table': 'History_Admin',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
