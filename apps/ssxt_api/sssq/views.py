from django.http import JsonResponse

def index(request):
    return JsonResponse({'status': 200, 'msg': 'OK'})
