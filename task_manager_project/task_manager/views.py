from django.shortcuts import render

def index(request):
    # Add your view logic here
    return render(request, '/Users/yohaansingla/Desktop/Django-Tasks/task_manager_project/task_manager/templates/index.html')  # Render the HTML template
