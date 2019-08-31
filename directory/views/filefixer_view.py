from django.shortcuts import render
from django.views.generic import View
from directory.app import filefixer
from django.http import QueryDict, JsonResponse
from django.core.files.storage import Storage, default_storage
from django.conf import settings
import os, re, pandas as pd, io, zipfile


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
            repaired_file = pd.read_csv(io.StringIO(broken_file), sep=';')
            repaired_file = repaired_file.iloc[:, [0, 1, 2]]
            
            path = Storage.get_available_name(default_storage, os.path.join('tmp', f.name))
            file_name = os.path.join(settings.MEDIA_ROOT, path)            
            repaired_file.to_csv(file_name, sep=';', index=False) 
            
            saved_files.append({"name": f.name, 
                                "data": repaired_file.values.tolist()
            })

            zf.write(file_name, os.path.basename(file_name))
            os.remove(file_name)

        zf.close()
    
        """tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        saved_files.append(tmp_file)


        ziped_files = filefixer.repair_csv(saved_files)  """ 

        """ qdict = QueryDict('', mutable=True)
        qdict.update(request.FILES)
        files = qdict.getlist("data_file[]")
        saved_files = []

        for f in files:
            path = default_storage.save(f'tmp/{f}', ContentFile(f.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            saved_files.append(tmp_file)


        ziped_files = filefixer.repair_csv(saved_files) """

        responseData = { 
            'initialPreview': [],
            'initialPreviewConfig': [],
            'initialPreviewThumbTags': [],
            'append': True,
            'urlDownload': os.path.basename(zf.filename),
            'graphData': saved_files,
        }

        return JsonResponse(responseData)

