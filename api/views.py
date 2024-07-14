from django.http import JsonResponse
from django.http import HttpResponse

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view, parser_classes

import langflow_output
import vectara


@api_view(["GET"])
def test(request):
    return JsonResponse({"message": "Hello, World!"})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={"question": openapi.Schema(type=openapi.TYPE_STRING)},
    ),
    responses={200: openapi.Response("Success")},
)
@api_view(["POST"])
def getResponseFromLangFlow(request):
    if "question" not in request.data:
        return JsonResponse({"error": "No question provided"}, status=400, safe=False)

    question = request.data["question"]
    response = langflow_output.getResponseFromQAFlow(question)
    return JsonResponse({"result": response}, safe=False, status=200)


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={"question": openapi.Schema(type=openapi.TYPE_STRING)},
    ),
    responses={200: openapi.Response("Success")},
)
@api_view(["POST"])
def getAgentCrewAdvice(request):
    if "question" not in request.data:
        return JsonResponse({"error": "No question provided"}, status=400, safe=False)

    question = request.data["question"]
    response = langflow_output.getResponseFromAgentCrew(question)
    return JsonResponse({"result": response}, safe=False, status=200)



@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={"file_text": openapi.Schema(type=openapi.TYPE_STRING)},
    ),
    responses={200: openapi.Response("Success")},
)
@api_view(["POST"])
def addFileTutorBrain(request):
    if "file_text" not in request.data:
        return JsonResponse({"error": "No file text provided"}, status=400, safe=False)
    
    file_text = request.data["file_text"]
    vectara.ResetCorpus()
    vectara.AddFile(file_text)

    return JsonResponse({"message": "Data has been successfully added to Tutor Brain"}, safe=False, status=200)


