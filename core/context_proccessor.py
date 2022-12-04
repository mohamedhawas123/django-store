from core.models import Category


def menu_links(request):
    linkes = Category.objects.all()
    return dict(linkes=linkes)
    