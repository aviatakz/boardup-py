from django.db import models
from django.contrib.auth.models import User
class Group(models.Model):
    name = models.CharField(max_length=400, default='Default')
    created_at = models.DateTimeField(auto_now_add=True)
User.groups
class UserGroup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

        # def to_json(self):
        #     return {
        #         'user': self.user,
        #         'group': self.group
        #     }