from django.db import migrations


def create_groups(apps, schema_editor):
Group = apps.get_model('auth', 'Group')
Permission = apps.get_model('auth', 'Permission')


def ensure(name, codenames):
g, _ = Group.objects.get_or_create(name=name)
g.permissions.set(Permission.objects.filter(codename__in=codenames))


post_crud = ['add_post', 'change_post', 'delete_post', 'view_post']
comment_crud = ['add_comment', 'change_comment', 'delete_comment', 'view_comment']


# Custom permission codename must exist (declared on Post.Meta.permissions)
ensure('Admin', list(Permission.objects.values_list('codename', flat=True)))
ensure('Editor', post_crud + comment_crud + ['can_publish'])
ensure('Author', ['add_post', 'change_post', 'view_post', 'add_comment', 'view_comment'])
ensure('Reader', ['view_post', 'view_comment'])


class Migration(migrations.Migration):
dependencies = [
('blog', '0001_initial'),
]


operations = [
migrations.RunPython(create_groups),
]
