Simplify this Django code.

    def create_user(username):
        u = PrometaUser.objects.filter(username=username)
        if u:
            user = u[0]
        else:
            user = PrometaUser.objects.create_user(
                username=username,
                email="username@example.com",
                password="newbie",
                name=username,
                is_student=True
            )
        return user