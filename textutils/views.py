# this file is created by Nishkarsh
from django.http import HttpResponse
from django.shortcuts import render
def index(request) :
    return render(request, 'index.html')

def analyze(request):
    val=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capfirst=request.POST.get('capfirst','off')
    lineremove=request.POST.get('lineremove','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcount','off')
    if removepunc=="on":
        analyzed_val = ""
        for c in val:
            if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9') or c.isspace():
                analyzed_val+=c
        val=analyzed_val
        params = {'analyzed': 'Removed Punctuation', 'value': analyzed_val}
    if capfirst=="on":
        analyzed_val=""
        for i in range(len(val)):
            analyzed_val+=val[i].upper()
        params = {'analyzed': 'Done Capitalization', 'value': analyzed_val}
        val=analyzed_val
    if lineremove=="on":
        analyzed_val = ""
        for ch in val:
            if(ch!='\n' and ch!='\r'):
                analyzed_val+=ch
        params = {'analyzed': 'Line Removed', 'value': analyzed_val}
        val=analyzed_val
    if spaceremove=="on":
        analyzed_val = ""
        for i,ch in enumerate(val):
            if not (val[i]==" " and  val[i+1]==" "):
                analyzed_val+=val[i]
        params = {'analyzed': 'Space Removed', 'value': analyzed_val}
        val=analyzed_val
    if charcount=="on":
        analyzed_val=0
        for c in val:
            if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'):
                analyzed_val+=1
        params = {'analyzed': 'Character Count', 'value': analyzed_val}
    return render(request, 'analyze.html', params)