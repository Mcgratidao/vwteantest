from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Create your models here

  
total_access_group = Group.objects.create(name='Acesso Total')
alternative_access_group = Group.objects.create(name='Acesso Alternativo')
user_with_total_access = User.objects.get(username='username1')
user_with_alternative_access = User.objects.get(username='username2')
user_with_total_access.groups.add(total_access_group)
user_with_alternative_access.groups.add(alternative_access_group)
