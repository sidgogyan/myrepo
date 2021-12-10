
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os, filecmp
import subprocess

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
            #   os.system('javac '+file)
            #  s = subprocess.check_output("javac "+file, shell = True)
            #  return 200
            try:
                output = subprocess.check_output(
                "javac "+file, stderr=subprocess.STDOUT, shell=True, timeout=3,
                universal_newlines=True)
            except subprocess.CalledProcessError as exc:
              return  "Status : FAIL", exc.returncode, exc.output
            else:
                return"Output: \n{}\n".format(output)
              
            
            
        # # elif lang == 'c' or lang == 'cpp':
        # #     os.system('gcc -o '+class_file+' '+file)
        #     if (os.path.isfile(class_file)):
        #         return 200
        #     else:
        #         return 400
        # else:
        #    return 404


# Create your views here.
@api_view(['POST'])
def method1(request):
    code=request.data.get('code')
    len1=request.data.get('len')
    if os.path.isfile("Main.java"):
        os.remove("Main.java")
    f = open("Main.java", "x")
    f.write(code)
    f.close()
    file = 'Main.java'
    # codes[compile(file,len1)]
    std=""
    try:
        output = subprocess.check_output(
            "javac "+file, stderr=subprocess.STDOUT, shell=True, timeout=3,
            universal_newlines=True)
    except subprocess.CalledProcessError as exc:
        std="Status : FAIL", exc.returncode, exc.output
    else:
        # std="Output: \n{}\n".format(output)
        std="compiled sucess"
    

    context={
        'msg':'we got data',
         'code':code,
         'len':len1,
         'std':std
         
         
    }

    return Response(context)
