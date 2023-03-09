from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from PIL import Image
from django.http import HttpResponse
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def upload_image(request):
    if request.method == 'POST':
        # Retrieve the uploaded file from the request
        try:
            uploaded_file = request.FILES['image']
            print("law")
        except KeyError:
            return HttpResponseBadRequest('Image file not found')

        # Verify that the uploaded file is an image
        if not uploaded_file.content_type.startswith('image/'):
            return HttpResponseBadRequest('Invalid image file')

        # Verify that the uploaded file is not too large
        if uploaded_file.size > 10 * 1024 * 1024:
            return HttpResponseBadRequest('File too large')

        # Process the image (resize to 500px width, convert to JPEG format)
        image = Image.open(uploaded_file)
        image = image.resize((500, int(500 * image.height / image.width)))
        image = image.convert('RGB')

        # Save the processed image to disk or to a database
        media_path = os.path.join(settings.MEDIA_ROOT, 'newfile.jpg')
        image.save(media_path)

        # Redirect to the success page
        return redirect('success')
    else:
        # If the request method is not POST, render the file upload form
        return render(request, 'upload_form.html')

def success_page(request):
    return render(request, 'success.html')