from django.shortcuts import render
from django.views.generic import View
from directory.app import filefixer
from django.http import QueryDict, JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os, zipfile


class FileFixerView(View):
    template_name = 'filefixer.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):   

        for k in request.session.items():
            print(k)   

        qdict = QueryDict('', mutable=True)
        qdict.update(request.FILES)
        files = qdict.getlist("data_file[]")
        saved_files = []

        for f in files:
            path = default_storage.save(f'tmp/{f}', ContentFile(f.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            saved_files.append(tmp_file)


        ziped_files = filefixer.repair_csv(saved_files)

        responseData = { 
            'initialPreview': [],
            'initialPreviewConfig': [],
            'initialPreviewThumbTags': [],
            'append': True,
            'urlDownload': ziped_files,
        }

        return JsonResponse(responseData)




""" class FileFixerView(TemplateView):
    template_name = "filefixer.html"

from django.shortcuts import render
from .config import UPLOAD_DIR 
import os
import pandas as pd


#File extension checker
def read_data(data_input, **kwargs):

    #dictionary of file formats
    read_map = {"xls": pd.read_excel, "xlsm": pd.read_excel, "xlsx": pd.read_excel,
                "csv": pd.read_csv}

    #getting the file extension
    extension = os.path.splitext(data_input)[1].lower()[1:]

    #check if file extension and document upload validation
    assert extension in read_map
    assert os.path.isfile(data_input)


def upload(request):

    if request.method == "POST" and request.FILES["data_file"]:

        if "data_file" not in request.FILES:
            return render(request, 'qwe/form.html')


        data = request.FILES["data_file"]

        if data == "":
            return render(request, 'qwe/form.html')

        #uploads the data in the specific directory
        os.path.join(UPLOAD_DIR, data)

        # TO-DO DATA PROCESSING HERE

        #Error: Assigning to function call which doesn't return
        df = read_data(data)

        return df.to_csv("asd.csv")

    else:

        return render(request, 'qwe/form.html') """


