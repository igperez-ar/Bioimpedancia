from django.shortcuts import render
from django.views.generic import View
from directory.app import filefixer
from django.http import QueryDict, JsonResponse
from django.core.files.storage import Storage, default_storage
from django.conf import settings
import os, re, pandas as pd, io, zipfile
import numpy as np

class FileFixerView(View):
    template_name = 'filefixer.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):  

        qdict = QueryDict('', mutable=True)
        qdict.update(request.FILES)
        files = qdict.getlist("data_file[]")
        saved_files = []

        zpath = Storage.get_available_name(default_storage, 'Bioimp.zip')
        path_zip = os.path.join(settings.MEDIA_ROOT, zpath)
        zf = zipfile.ZipFile(path_zip, "w")

        p = re.compile(r'(\D),(\D)')

        for f in files:
            broken_file = p.sub(r'\1;\2', f.read().decode('utf-8'))
            data = pd.read_csv(io.StringIO(broken_file), sep=';')
            repaired_file = data.iloc[:, [0, 1, 2]]
            
            path = Storage.get_available_name(default_storage, os.path.join('tmp', f.name))
            file_name = os.path.join(settings.MEDIA_ROOT, path)            
            repaired_file.to_csv(file_name, sep=';', index=False)

            spectrum = data.iloc[:, [0]]
            z = data.iloc[:, [1]]

            impedancia_data = {
                'x': spectrum,
                'y': z
            }
            
            impedancia_data_log = {
                'x': np.log10(spectrum),
                'y': z
            }

            fase_data = {
                'x': spectrum,
                'y': data.iloc[:, [2]]
            }

            cole_cole_data = {
                'x': data.iloc[:, [3]],
                'y': data.iloc[:, [4]]
            }

            graphData = {
                'impedancia_data' : impedancia_data,
                'impedancia_data_log': impedancia_data_log,
                'fase_data': fase_data,
                'cole_cole_data': cole_cole_data,
            }
            
            graphs.append({
                    "name": f.name,
                    "data": graphData
            })

            print(graphs)

            zf.write(file_name, os.path.basename(file_name))
            os.remove(file_name)

        zf.close()


        responseData = { 
            'initialPreview': [],
            'initialPreviewConfig': [],
            'initialPreviewThumbTags': [],
            'append': True,
            'urlDownload': os.path.basename(zf.filename),
            'graphs': graphs,
        }

        return JsonResponse(responseData)

