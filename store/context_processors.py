from .views import Category


def categoy_navbar(request):
    categoy_navbar = Category.objects.all()
    return {'categoy_navbar':categoy_navbar }