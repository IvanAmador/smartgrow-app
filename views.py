from .models import Plant

def index(request):
    plants = Plant.objects.all()
    return render(request, 'index.html', {'plants': plants})