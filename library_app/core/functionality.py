def get_creator_user(user):
    return user.groups.filter(name='Library Admin').exists()
