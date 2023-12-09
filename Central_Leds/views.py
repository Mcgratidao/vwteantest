from django.shortcuts import render

# Create your views here

from django.contrib.auth.decorators import permission_required, user_passes_test

   def total_access_check(user):
       return user.groups.filter(name='Acesso Total').exists()

   @user_passes_test(total_access_check)
   def total_access_view(request):
       # Lógica para usuários com acesso total
       pass

   def alternative_access_check(user):
       return user.groups.filter(name='Acesso Alternativo').exists()

   @user_passes_test(alternative_access_check)
   def alternative_access_view(request):
       # Lógica para usuários com acesso alternativo
       pass.
