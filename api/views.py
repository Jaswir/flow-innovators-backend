from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes

import langflow_output

@api_view(["GET"])
def test(request):
    return JsonResponse({"message": "Hello, World!"})


def getResponseFromLangFlow(question):
    response = langflow_output.getResponseFromLangFlow(question)
    return response