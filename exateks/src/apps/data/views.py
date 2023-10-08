import json

from typing import Optional

from django.http import HttpResponse


# Create your views here.

def hello(request):
    data = {
        "Company": "Exateks",
    }

    return HttpResponse(json.dumps(data, sort_keys=False, indent=4))
