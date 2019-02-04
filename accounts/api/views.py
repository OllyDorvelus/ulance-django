from rest_framework import generics
from .serializers import User, UserModelSerializer, UserCreateSerializer, UserLoginSerializer
from ulance import pagination
from . import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class UserModelListAPIView(generics.ListAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all().order_by('username')
    pagination_class = pagination.StandardResultsPagination


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.UserCreatePermission]


class UserLoginAPIView(APIView):
   # permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


