from django.shortcuts import render
from .models import Video
from http.client import HTTPResponse
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
# from tablib import Dataset
# from .resources import VideoResource
from django.contrib.postgres.search import SearchQuery, SearchVector,SearchRank,SearchHeadline

def index(request):
    q = request.GET.get('q', None)

    if q:
        q=str(q)
        q.replace('+'," ")
        vector=SearchVector('description','title',)
        query=SearchQuery(q,search_type='plain')
        search_headline = SearchHeadline('description',query,start_sel='<b>',stop_sel='</b>',max_fragments=1)
        

        # videos = Video.objects.annotate(rank=SearchRank(vector, query)).annotate(headline=search_headline).filter(rank__gte=0.7).order_by('-rank')

        
        # videos = Video.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')
        videos=Video.objects.annotate(search=vector).filter(search=query).annotate(headline=search_headline)
        # videos=Video.objects.filter(title__search=q)
        
    else:
        videos=None

    context={'videos':videos}
    return render(request,'projectApp/index.html',context)
    

def index2(request):
        q=request.GET.get('q')
        return render(request, 'projectApp/index2.html')

def add_video(request):
    if request.method == 'POST':
            if request.POST.get('youtube_id_html') and request.POST.get('title_html') and request.POST.get('description_html'):
                v=Video(youtube_id=request.POST.get('youtube_id_html'),title= request.POST.get('title_html'),description= request.POST.get('description_html'))
                
                v.save()
                
    return render(request, 'projectApp/inde1.html')

# Create your views here.

 
def Import_Excel_pandas(request):
     
    if request.method == 'POST' and request.FILES['myfile']: 
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(filename)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Video.objects.create(youtube_id=dbframe.id,title=dbframe.t,description=dbframe.desc )           
            obj.save()
        return render(request, 'projectApp/Import_excel_db.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'projectApp/Import_excel_db.html',{})

 
# def Import_excel(request):
#     if request.method == 'POST' :
#         v =VideoResource()
#         dataset = Dataset()
#         new_video = request.FILES['myfile']
#         data_import = dataset.load(new_video.read())
#         result = v.import_data(dataset,dry_run=True)
#         if not result.has_errors():
#             v.import_data(dataset,dry_run=False)        
#     return render(request, 'projectApp/Import_excel_db.html',{})