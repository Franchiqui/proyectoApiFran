from django.shortcuts import render
from django.http import JsonResponse
from .models import scanTexto_func
from .forms import ImageUploadForm


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            extracted_text = scanTexto_func(image)
            return render(request, 'result.html', {'extracted_text': extracted_text})
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload_image.html', {'form': form})


def extract_text_from_image(request):
    if request.method == 'POST':
        image_path = request.FILES['image'].temporary_file_path()
        extracted_text = scanTexto_func(image_path)
        return JsonResponse({'extracted_text': extracted_text})


# Create your views here.
