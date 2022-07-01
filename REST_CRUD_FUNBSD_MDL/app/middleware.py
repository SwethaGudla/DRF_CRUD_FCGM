from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
import jwt
from django.conf import settings
class AddValidationMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        try:
            print("++++tokenn11+++")
            if settings.AUTH == True:
                # print("++++tokenn+++\n",request.META)
                print(request.META["HTTP_AUTH_TOKEN"])
                if "HTTP_AUTH_TOKEN" in request.META:
                    
                    print("++++toekn+++")
                    token = request.META["HTTP_AUTH_TOKEN"].replace("Bearer ","")
                    try:
                        print("+++++++token")
                        print(token)
                        print(settings.SECRET_KEY)
                        # x = jwt.decode(token,settings.SECRET_KEY, algorithms=["HS256"])
                        # token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0OTU5NDU2LCJpYXQiOjE2NTQ5Nzg5NTYsImp0aSI6IjUyYTgyNzUwODE2MTRjYmE4OWNiYjZlNjc0OTI5OWNmIiwidXNlcl9pZCI6MiwidXNlciI6ImFkbWluIiwiZGF0ZSI6IjIwMjItMDYtMTEiLCJlbWFpbCI6ImFkbWluQG9qYXMuY29tIn0.BAFHBlc8WLDvEHk9kpO6kpK9wObiqcDerlb3DParbhU"
                        token.replace(" ","")
                        secret="django-insecure-ck!-4rbo!6-wa&rvys41*sm0o!2#jg!qc8u!ux4ugaoe=84-cm"
                        x=jwt.decode(token,secret,algorithms=["HS256"])
                        print(x)
                                           
                    except Exception as Error:
                        return HttpResponseBadRequest(Error)
                    if "email" in x:
                        if "@ojas.com" in x['email']:
                            return self.get_response(request.META)
                        else:
                            raise PermissionDenied()
                return HttpResponseBadRequest(request)
            else:
                return self.get_response(request)
        except Exception as Error:
            raise "Error in Authentication"
    def process_exception(self, request,exception):
        return HttpResponse("In Exception")