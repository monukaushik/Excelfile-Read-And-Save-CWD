from django.shortcuts import render
import pandas as pd


def index(request):
   if request.method=='POST':
      file = request.FILES['file']
      src_file = pd.ExcelFile(file)
      writer = pd.ExcelWriter('destination.xlsx', engine='xlsxwriter')
      for sheet_name in src_file.sheet_names:
            df = pd.read_excel(src_file, sheet_name=sheet_name)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
      writer.save()

   return render(request,'index.html')
