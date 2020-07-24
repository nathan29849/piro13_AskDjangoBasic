from django.http import HttpResponse
from .models import Item
from django.shortcuts import render
# import pandas as pd
# from io import StringIO

# from urllib.parse import quote
from django.shortcuts import render


# Create your views here.
def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)  # icontains는 ignore문자 : 영어로 치면 대소문자 구별 안하겠다는 의미
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })


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
