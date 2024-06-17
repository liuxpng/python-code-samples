class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


user_list = [
    User(31), User(22), User(13), User(54),
]

from operator import attrgetter

print(sorted(user_list, key=attrgetter('user_id')))
print(sorted(user_list, key=lambda v: v.user_id))
