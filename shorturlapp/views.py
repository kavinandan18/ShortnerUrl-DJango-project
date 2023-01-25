
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import URLs
import hashlib
# Create your views here.

def home(request):
	return render(request, 'index.html')

def short(request):
	url = request.GET["url"]
	hashObject = hashlib.sha256(str(url).encode('utf-8'))
	shrinkedURL = hashObject.hexdigest()[:8]

	try:
		check = URLs.objects.get(shrinkedURL = shrinkedURL)
	except URLs.DoesNotExist:
		entry = URLs(shrinkedURL = shrinkedURL, targetURL=url)
		entry.save()
	return render(request, 'index.html',{'shrinkedURL':shrinkedURL})

def retrieve(request,inputURL):

	target = get_object_or_404(URLs, shrinkedURL = inputURL)
	targetURL = target.targetURL
	if(targetURL[:4] != 'http'):
		targetURL = 'http://'+targetURL
	return redirect(targetURL)