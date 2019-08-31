import re, os, csv, zipfile
from django.conf import settings 
from django.core.files.storage import Storage, default_storage
from fpdf import FPDF, HTMLMixin

def repair_csv(files):
    p = re.compile(r'(\D),(\D)')
    path = Storage.get_available_name(default_storage, 'Bioimp.zip')
    path_zip = os.path.join(settings.MEDIA_ROOT, path)
    zf = zipfile.ZipFile(path_zip, "w")
    
    for f in files:
        with open(f, "r+") as openFile:
            new_content = "Frecuency ;Impedance ;Phase"
            next(openFile)
            
            for line in openFile:
                if len(line.strip()) != 0 :
                    line = line.strip()
                    column = re.split(p, line)
                    new_content = f"{new_content} \n{column[0]} ;{column[1]} ;{column[2]}"

            openFile.seek(0)
            openFile.write(new_content)
            openFile.close()

        zf.write(f, os.path.basename(f))
        os.remove(f)
    
    zf.close()
    return os.path.basename(zf.filename)


def toPDF(file_in):
    csv_in   = file_in
    pdf_out  = "Bioimpedancia - Archivo reparado.pdf"
    title    = "Bioimpedancia - Archivo reparado"
    subject  = "Subject"
    author   = "Reparado por http://bioimpedancia.untdf.edu.ar/"
    keywords = "Bioimpedancia"
    creator  = "Reparado por http://bioimpedancia.untdf.edu.ar/"

    header = """
    <table align="center" width="100%">
    <thead><tr>
    <th width="24%">Frecuency</th>
    <th width="38%">Impedance</th>
    <th width="38%">Phase</th>
    </tr></thead>
    """

    counter = 1
    split = ";"
    join = "</td><td align=\"center\">"
    html_out = ""

    iterFile = open(csv_in)
    next(iterFile)

    for line in iterFile:
        if len(line.strip()) != 0 :
            line = line.strip()
            column = line.split(split)
            
            frecuency = column[0]
            impedance = column[1]
            phase     = column[2] 

            counter = counter + 1
            mod = counter % 2
            if mod == 1:
                bgcolor = "<tr bgcolor=\"#FFFFFF\"><td align=\"center\">"
            else:
                bgcolor = "<tr bgcolor=\"#E1E1E1\"><td align=\"center\">"

            if counter == 1000:
                over_flow = "<tr></tr>\n" * 10
            else:
                over_flow = ""

            row = (bgcolor + frecuency + join + impedance + join \
                + phase + "</td></tr>\n" + over_flow)

            html_out = html_out + row

    footer = "</tbody></table>"
    html = header + html_out + footer

    class MyFPDF(FPDF, HTMLMixin):

        def footer(self):
            self.set_y(-25)  #-25
            self.set_font('Arial','I',10)
            self.set_text_color(0,0,0)
            self.cell(0,10,'Página %s de {nb}' % self.page_no(),0,0,'C')

    pdf = MyFPDF('P','mm','A4')
    pdf.set_top_margin(margin=18)  #18
    pdf.set_auto_page_break(True, 27) #27
    pdf.add_page()
    pdf.alias_nb_pages()

    pdf.image('isologotipo.png', 15, 8, 60)
    pdf.image('idei.png', 150, 8, 20)
    pdf.set_font("Arial", style="B", size=20)
    pdf.cell(200, 5, 'Bioimpedancia', align='C', ln=1)
    pdf.set_font("Arial", size=7)
    pdf.cell(200, 4,' ', ln=1)
    pdf.cell(136)
    pdf.cell(170, 3, 'Instituto de Desarrollo', ln=1)
    pdf.cell(135)
    pdf.cell(170, 3, 'Económico e Innovación', ln=1)
    pdf.cell(200, 10,' ', ln=1)
    pdf.set_font("Arial", style="I", size=12)
    pdf.cell(200, 5,'Archivo reparado a través de', ln=1)
    pdf.cell(200, 5,'http://bioimpedancia.untdf.edu.ar/', ln=1)

    pdf.set_title(title)
    pdf.set_subject(subject)
    pdf.set_author(author)
    pdf.set_keywords(keywords)
    pdf.set_creator(creator)
    pdf.write_html(html)
    pdf.output(pdf_out)


""" def repair_csv(files):
    p = re.compile(r'(\D),(\D)')
    path = Storage.get_available_name(default_storage, 'Bioimp.zip')
    path_zip = os.path.join(settings.MEDIA_ROOT, path)
    zf = zipfile.ZipFile(path_zip, "w")
    
    for f in files:
        with open(f, "r+") as openFile:
            new_content = "Frecuency ;Impedance ;Phase"
            next(openFile)
            
            for line in openFile:
                if len(line.strip()) != 0 :
                    line = line.strip()
                    column = p.sub(r'\1;\2', line).split(";")
                    new_content = f"{new_content} \n{column[0]} ;{column[1]} ;{column[2]}"

            openFile.seek(0)
            openFile.write(new_content)
            openFile.close()

        zf.write(f, os.path.basename(f))
        os.remove(f)
    
    zf.close()
    return os.path.basename(zf.filename) """