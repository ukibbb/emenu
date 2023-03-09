from django.db import migrations


def load_data(apps, schema_editor):
    MenuItem = apps.get_model("menu_items", "MenuItem")

    MenuItem.objects.create(
        name="Tomato Soup",
        description="Tomato soup.",
        price=20.0,
        is_vegetarian=True,
        preparation_time="00:30:00",
    ),
    MenuItem.objects.create(
        name="Sznycel",
        description="Piece of meat.",
        price=23.0,
        is_vegetarian=False,
        preparation_time="00:50:00",
    ),
    MenuItem.objects.create(
        name="Salomon",
        description="Piece of fish",
        price=19.0,
        is_vegetarian=True,
        preparation_time="01:50:00",
    ),


class Migration(migrations.Migration):
    dependencies = [("menu_items", "0001_initial")]
    operations = [migrations.RunPython(load_data)]
