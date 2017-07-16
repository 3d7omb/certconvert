# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView
from django.http import Http404, HttpResponse
from django.contrib import messages

from .forms import UploadForm

from OpenSSL import crypto
import StringIO
# Create your views here.

def index(request):
    return render(request, 'tools/index.html', {})

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            #Reading POST data
            cert = request.FILES.get('file').read()
            password = request.POST.get('password')
            if request.FILES['file'].name.endswith('.pfx'):
                try:
                    try:
                        try:
                            #Convert pfx to pem and key
                            p12 = crypto.load_pkcs12(cert, password)
                            crt = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
                            key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())
                        except:
                            #Password incorrect error
                            messages.error(request, "Password incorrect")
                            return render(request, 'tools/upload.html', {'form': form})
                        #Create File
                        download = StringIO.StringIO()
                        download.write(crt)
                        download.write(key)
                        contents = download.getvalue()
                        #Create response
                        response = HttpResponse(contents)
                        response['Content-Disposition'] = "attachment; filename=cert.pem"
                        #Return response
                        return response
                    except:
                        #Failed to make file error
                        messages.error(request, "Failed to make file")
                        return render(request, 'tools/upload.html', {'form': form})
                except:
                    #Catch for weird errors
                    messages.error(request, "Something fucked up")
                    return render(request, 'tools/upload.html', {'form': form})
            else:
                #Incorrect file type error - Only temporary. Support for multiple types soon!
                messages.error(request, "File must be PFX")
    else:
        #Creating form if no POST
        form = UploadForm()
    return render(request, 'tools/upload.html', {'form': form})
