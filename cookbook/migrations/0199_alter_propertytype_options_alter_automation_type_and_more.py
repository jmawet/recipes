# Generated by Django 4.1.10 on 2023-08-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0198_propertytype_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='type',
            field=models.CharField(
                choices=[
                    ('FOOD_ALIAS',
                     'Food Alias'),
                    ('UNIT_ALIAS',
                     'Unit Alias'),
                    ('KEYWORD_ALIAS',
                     'Keyword Alias'),
                    ('DESCRIPTION_REPLACE',
                     'Description Replace'),
                    ('INSTRUCTION_REPLACE',
                     'Instruction Replace'),
                    ('NEVER_UNIT',
                     'Never Unit'),
                    ('TRANSPOSE_WORDS',
                     'Transpose Words')],
                max_length=128),
        ),
    ]
