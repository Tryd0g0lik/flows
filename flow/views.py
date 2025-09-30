from django.shortcuts import render

from flow.models_views.types import TypeFlowModel

# Create your views here.


def main(request):
    types = TypeFlowModel.objects.all()
    return render(request, "flow/typeflow.html", {"types": types})
