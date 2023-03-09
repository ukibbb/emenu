from django.db import migrations


def load_data(apps, schema_editor):
    Menu = apps.get_model("menus", "Menu")
    MenuItem = apps.get_model("menu_items", "MenuItem")

    vegetarian = MenuItem.objects.create(
        name="Vegetarian soup",
        description="With fish.",
        price=11.0,
        is_vegetarian=True,
        preparation_time="00:10:00",
    )
    schabowy = MenuItem.objects.create(
        name="Schabowy",
        description="Schabowy",
        price=19.0,
        is_vegetarian=False,
        preparation_time="1:22:00",
    )
    mielone = MenuItem.objects.create(
        name="Mielone",
        description="Pyszniutkie",
        price=22,
        is_vegetarian=False,
        preparation_time="2:00:00",
    )

    Menu.objects.create(
        name="Vegetarian", description="Menu with food without meat"
    ).items.add(vegetarian)
    Menu.objects.create(name="Meatfull", description="A lot of meat in this menu")
    Menu.objects.create(name="Polish", description="Polish Menu").items.add(
        schabowy, mielone
    )


class Migration(migrations.Migration):
    dependencies = [("menus", "0001_initial")]
    operations = [migrations.RunPython(load_data)]
