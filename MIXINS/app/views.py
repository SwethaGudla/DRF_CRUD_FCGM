from django.shortcuts import render
from app.models import StdModel
from app.serializers import StdSerializer
from rest_framework import mixins,generics
# Create your views here.
class StdListMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = StdModel.objects.all()
    serializer_class = StdSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StdDetailedMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset=StdModel.objects.all()
    serializer_class = StdSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)