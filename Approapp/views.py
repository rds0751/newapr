from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf  # created in step 4


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        data = {
            'today': "today",
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('invoice.html', data)
        return HttpResponse(pdf, content_type="application/pdf")
'''if pdf:
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Invoice_%s.pdf" %("1234")
    content = "inline; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response
return HttpResponse("Not Found")'''
