def cleanup_social_account(backend, uid, user=None, *args, **kwargs):
    print(kwargs)
    print(user)
    user.photo = kwargs['response']['picture']
    user.save()
    return {'user': user}
