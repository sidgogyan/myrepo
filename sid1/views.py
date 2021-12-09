
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def method1(request):
    code=request.data.get('code')
    len1=request.data.get('len')
    context={
        'msg':'we got data',
         'code':code,
         'len':len1
         
    }

    return Response(context)
