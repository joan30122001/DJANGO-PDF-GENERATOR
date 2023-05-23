from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import TitleForm, SubTitleForm, CoverForm, BoardTitleForm, BoardElementForm
from .models import Title, SubTitle, Cover, BoardTitle, BoardElement
from .forms import RangeTitleForm, RangeSubTitleForm, RangeBoardTitleForm, RangeBoardElementForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
import os
from django.conf import settings
from django.template.loader import get_template
from django.template import Template
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Paragraph
from reportlab.lib.styles import ParagraphStyle
from PyPDF2 import PdfReader, PdfWriter
from django.template import Context
from reportlab.lib.units import inch
from .utils import fetch_resources
# from weasyprint import HTML




def cover(request):
    if request.method == 'POST':
        form = CoverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CoverForm()
            # return redirect('input_list')
    else:
        form = CoverForm()
    return render(request, 'cover.html', {'form': form})



def title(request):
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('input_list')
    else:
        form = TitleForm()
    return render(request, 'title.html', {'form': form})



def subtitle(request):
    if request.method == 'POST':
        form = SubTitleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('input_list')
    else:
        form = SubTitleForm()
    return render(request, 'subtitle.html', {'form': form})



def boardtitle(request):
    if request.method == 'POST':
        form = BoardTitleForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('input_list')
    else:
        form = BoardTitleForm()
    return render(request, 'boardtitle.html', {'form': form})



def boardelement(request):
    if request.method == 'POST':
        form = BoardElementForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('input_list')
    else:
        form = BoardElementForm()
    return render(request, 'boardelement.html', {'form': form})



# def render_to_pdf(template_src, context_dict={}):
#     if template_src is None:
#         html = context_dict['html']
#     else:
#         template = get_template(template_src)
#         html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="preview.pdf"'
#     pisa_status = pisa.CreatePDF(
#         html, dest=response, encoding='utf-8'
#     )
#     if pisa_status.err:
#         return HttpResponse('Failed to generate PDF', status=500)
#     return response



def preview(request):
    # cover = Cover.objects.all()
    # cover = Cover.objects.get(id=cover_id)
    cover = Cover.objects.first()

    titles = Title.objects.all()
    subtitles_by_title = {}
    for title in titles:
        subtitles_by_title[title] = SubTitle.objects.filter(title=title)
    range_title_form = RangeTitleForm()
    range_subTitle_form = RangeSubTitleForm()

    # viens d'être ajouté
    boardtitles = BoardTitle.objects.all()
    boardelements_by_boardtitle = {}
    for boardtitle in boardtitles:
        boardelements_by_boardtitle[boardtitle] = BoardElement.objects.filter(boardtitle=boardtitle)
    range_boardtitle_form = RangeBoardTitleForm()
    range_boardelement_form = RangeBoardElementForm()
    # fin de l'ajout

    # viens d'être ajouté bis
    # subtitles = SubTitle.objects.all()
    # boardtitles_by_subtitle = {}
    # for subtitle in subtitles:
    #     boardtitles_by_subtitle[subtitle] = BoardTitle.objects.filter(subtitle=subtitle)
    # range_subTitle_form = RangeSubTitleForm()
    # range_boardtitle_form = RangeBoardTitleForm()
    # fin de l'ajout

    context = {
        'subtitles_by_title': subtitles_by_title,
        'range_title_form': range_title_form,
        'range_subTitle_form': range_subTitle_form,
        'cover': cover,

        'boardelements_by_boardtitle': boardelements_by_boardtitle,
        'range_boardtitle_form': range_boardtitle_form,
        'range_boardelement_form': range_boardelement_form,

        # 'boardtitles_by_subtitle': boardtitles_by_subtitle,
    }
    return render(request, 'preview.html', context)



# def download_pdf(request):
#     # cover = Cover.objects.all()

    # cover = Cover.objects.first()

    # titles = Title.objects.all()
    # subtitles_by_title = {}
    # for title in titles:
    #     subtitles_by_title[title] = SubTitle.objects.filter(title=title)
    # range_title_form = RangeTitleForm()
    # range_subTitle_form = RangeSubTitleForm()
    # context = {
    #     'subtitles_by_title': subtitles_by_title,
    #     'range_title_form': range_title_form,
    #     'range_subTitle_form': range_subTitle_form,
    #     'cover': cover,
    # }
#     pdf = render_to_pdf('pdf.html', context)
#     return pdf


    # Render only the desired div
    # html = render(request, 'preview.html', context)
    # div_id = 'to_generate'  # Replace with the ID of the desired div
    # start_tag = '<div id="{}">'.format(div_id)
    # end_tag = '</div>'
    # start_index = html.content.decode().find(start_tag)
    # end_index = html.content.decode().find(end_tag, start_index) + len(end_tag)
    # div_html = html.content.decode()[start_index:end_index]
    # # Generate the PDF from the div HTML
    # pdf = render_to_pdf(None, {'html': div_html})
    # return pdf



def generate_pdf(request):
    template_path = 'pdf.html'
    cover = Cover.objects.first()
    titles = Title.objects.all()
    subtitles_by_title = {}
    for title in titles:
        subtitles_by_title[title] = SubTitle.objects.filter(title=title)
    range_title_form = RangeTitleForm()
    range_subTitle_form = RangeSubTitleForm()



    # viens d'être ajouté
    boardtitles = BoardTitle.objects.all()
    boardelements_by_boardtitle = {}
    for boardtitle in boardtitles:
        boardelements_by_boardtitle[boardtitle] = BoardElement.objects.filter(boardtitle=boardtitle)
    range_boardtitle_form = RangeBoardTitleForm()
    range_boardelement_form = RangeBoardElementForm()
    # fin de l'ajout



    context = {
        'subtitles_by_title': subtitles_by_title,
        'range_title_form': range_title_form,
        'range_subTitle_form': range_subTitle_form,
        'cover': cover,

        'boardelements_by_boardtitle': boardelements_by_boardtitle,
        'range_boardtitle_form': range_boardtitle_form,
        'range_boardelement_form': range_boardelement_form,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="preview.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response.write(result.getvalue())
        return response
    return HttpResponse('Error generating PDF')



def template(request):
    return render(request, 'template.html')