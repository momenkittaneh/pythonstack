from django.shortcuts import render
from time import gmtime, strftime
from django.utils import timezone

    
def index(request):
    now = timezone.now()
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
	"new":now
    }
    return render(request,'index.html', context)
