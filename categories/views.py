from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category

def categories(request):
    all_categories = Category.objects.all()
    return Response(
        {
            "ok": True,
            "categories": Category.objects.all(),
        }
    )
