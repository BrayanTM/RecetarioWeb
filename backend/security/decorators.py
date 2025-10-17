from functools import wraps
from django.http import JsonResponse
from http import HTTPStatus
from jose import jwt
import time
import os


def logging_decorator():
    def method(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            req = args[0]

            if not req.headers.get('Authorization') or req.headers.get('Authorization') == None:
                return JsonResponse({"error": "Authorization header missing"}, status=HTTPStatus.UNAUTHORIZED)
            
            header = req.headers.get('Authorization').split(' ')

            try:
                resolved_token = jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=HTTPStatus.UNAUTHORIZED)

            if int(resolved_token["exp"]) > int(time.time()):
                return func(request, *args, **kwargs)
            else:
                return JsonResponse({"error": "Token has expired"}, status=HTTPStatus.UNAUTHORIZED)


        return _decorator
    return method