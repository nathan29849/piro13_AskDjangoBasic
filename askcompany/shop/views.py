from django.http import HttpResponse
# import pandas as pd
# from io import StringIO

# from urllib.parse import quote
from django.shortcuts import render

# Create your views here.
def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

# def response_csv(request):
#     df = pd.DataFrame([
#         [100, 110, 120],
#         [200, 210, 220],
#         [300, 310, 320],
#     ])
#
#     io = StringIO()
#     df.to_csv(io)
#     io.seek(0)
#
#     response = HttpResponse(io, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename*=utf-8""{}'.format(encoded_filename)
#     return response

# def response_excel(request):
#     filepath = '/other/path/excel.xls'
#     filename = os.path.basename(filepath)
#
#     with open(filepath, 'rb') as f:
#         response = HttpResponse(f, content_type='application/vnd.ms-excel')
#
#         encoded_filename = quote(filename)
#         response['Content-Disposition'] = 'attachment; filename*=utf-8""{}'.format(encoded_filename)
#
#     return response
