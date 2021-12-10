
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os, filecmp

codes = {200:'success',404:'file not found',400:'error',408:'timeout'}



def compile(file,lang):
    if lang == 'java':
        class_file = file[:-4]+"class"
    elif lang == 'c':
        class_file = file[:-2]
    elif lang=='cpp':
        class_file = file[:-4]

    if (os.path.isfile(class_file)):
        os.remove(class_file)
    if (os.path.isfile(file)):
        if lang == 'java':
            os.system('javac '+file)
        elif lang == 'c' or lang == 'cpp':
            os.system('gcc -o '+class_file+' '+file)
        if (os.path.isfile(class_file)):
            return 200
        else:
            return 400
    else:
        return 404


# Create your views here.
@api_view(['POST'])
def method1(request):
    code=request.data.get('code')
    len1=request.data.get('len')
    f = open("Main.java", "x")
    f.write(code)
    f.close()
    file = 'Main.java'
    res=codes[compile(file,len1)]

    context={
        'msg':'we got data',
         'code':code,
         'len':len1,
         'res':res
         
    }

    return Response(context)
