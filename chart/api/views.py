from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.generics import ListAPIView
from rest_framework import permissions

from chart.models import datas
from chart.api.serializers import DatasSerialzer


# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def api_datas_view(request):
#
#     try:
#         data = datas.objects.get()
#     except datas.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = DatasSerialzer(data)
#         return Response(serializer.data)

class api_datas_view(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = datas.objects.all()
    serializer_class = DatasSerialzer
    search_fields = ['number', 'value']




@api_view(['POST'])
def api_create_datas_view(request):
    data_obj = datas()

    if request.method == "POST":
        serializer = DatasSerialzer(data_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
