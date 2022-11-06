from django.http import JsonResponse
from .serializers import FieldSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(["POST"])
def endpoint(request):
    serializer = FieldSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    x = serializer.validated_data['x']
    y = serializer.validated_data['y']
    operation_type = serializer.validated_data['operation_type']
    if operation_type == 'addition':
        result = x + y
    elif operation_type == 'subtraction':
        result = x - y
    elif operation_type == 'multiplication':
        result = x * y

    return Response({
        "slackUsername": "Jude_olowo",
        "operation_type": operation_type,
        "result": result
    }, status=status.HTTP_200_OK)