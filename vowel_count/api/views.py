from django.http.response import JsonResponse

def vowel_count(request):
    return JsonResponse({"message": "Welcome to Vowel Count API service!"})