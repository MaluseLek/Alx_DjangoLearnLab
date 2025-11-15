# Role-Based Access Control
#
#
def is_role(user, role_name):
    return hasattr(user, 'userprofile') and user.userprofile.role == role_name


# Admin-only view 
@user_passes_test(lambda u: is_role(u, 'admin'))
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html')