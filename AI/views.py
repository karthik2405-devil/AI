from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

def upload_image(request):
    if request.method == 'POST':
        # Retrieve the uploaded file from the request
        try:
            uploaded_file = request.FILES['image_file']
        except KeyError:
            return HttpResponseBadRequest('Image file not found')

        # Verify that the uploaded file is an image
        if not uploaded_file.content_type.startswith('image/'):
            return HttpResponseBadRequest('Invalid image file')

        # Verify that the uploaded file is not too large
        if uploaded_file.size > 10 * 1024 * 1024:
            return HttpResponseBadRequest('File too large')

        # Process the image as required (resize, crop, etc.)
        # Save the processed image to disk or to a database

        # Redirect to a success page
        return redirect('success')
    else:
        # If the request method is not POST, render the file upload form
        return render(request, 'upload_form.html')
