from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from django.conf import settings

from supabase import create_client, Client

from hashlib import sha512

import uuid
import datetime

supabase: Client = create_client(settings.SUPABASE_URL,
                                    settings.SUPABASE_KEY).schema("public")

class SBaseSelectAll(APIView):
    """
        Представление, позволяющее получить все данные из указанной в эндпоинте таблице.
    """

    def get(self, request: Request, table: str):
        try:
            response = supabase.table(table) \
                            .select("*").execute()
            
            return Response({
                "data": response.data,
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(f"Произошла ошибка при запросе SBaseSelectAll\nОшибка: {e}\nВремя: {datetime.datetime.now()}")
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SBaseInsert(APIView):
    """
        Представление, позволяющее записать данные в БД
    """
    def post(self, request: Request, table: str):
        try:
            data = request.data

            if "password" in data:
                salt = bytes(str(uuid.uuid4()), settings.BYTES_ENCODING)
                data["password"] = str(sha512(bytes(data["password"], settings.BYTES_ENCODING) + salt).hexdigest()) + ':' + salt.decode(settings.BYTES_ENCODING)

            supabase.table(table) \
            .insert(data) \
            .execute()

            return Response(status=status.HTTP_200_OK)
        
        except Exception as e:
            print(f"Произошла ошибка при запросе SBaseInsert\nОшибка: {e}\nВремя: {datetime.datetime.now()}")
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SBaseUpdate(APIView):
    """
        Представление, повзоляющее обновить данные в бд
    """
    def put(self, request: Request, table: str):
        try:
            data = request.data

            if "password" in data:
                del data["password"]

            core = supabase.table(table) \
            .update(data) \
            
            if "login" in data:
                core.eq("login", data["login"]) \
                .execute()

            elif "id" in data:
                core.eq("id", data["id"]) \
                .execute()

            elif "login" in data and "id" in data:
                core.eq("id", data["id"]) \
                .execute()

            return Response(status=status.HTTP_200_OK)
            
        except Exception as e:
            print(f"Произошла ошибка при запросе SBaseUpdate\nОшибка: {e}\nВремя: {datetime.datetime.now()}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SBaseDelete(APIView):
    """
        Представление, позволяющее удалить строчку из бд
    """

    def delete(self, request: Request, table: str):
        try:
            data = request.data

            if "password" in data:
                del data["password"]

            core = supabase.table(table) \
            .delete() \
            
            if "login" in data:
                core.eq("login", data["login"]) \
                .execute()

            elif "id" in data:
                core.eq("id", data["id"]) \
                .execute()

            elif "login" in data and "id" in data:
                core.eq("id", data["id"]) \
                .execute()

            return Response(status=status.HTTP_200_OK)
            
        except Exception as e:
            print(f"Произошла ошибка при запросе SBaseDelete\nОшибка: {e}\nВремя: {datetime.datetime.now()}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
