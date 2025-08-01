import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

"""f"""
class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AchievementCat',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('achievement', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='cats.achievement'
                )),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(max_length=16)),
                ('color', models.CharField(max_length=16)),
                ('birth_year', models.IntegerField()),
                ('image', models.ImageField(
                    default=None,
                    null=True,
                    upload_to='cats/images/'
                )),
                ('achievements', models.ManyToManyField(
                    through='cats.AchievementCat',
                    to='cats.Achievement'
                )),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='cats',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
        migrations.AddField(
            model_name='achievementcat',
            name='cat',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='cats.cat'
            ),
        ),
    ]
