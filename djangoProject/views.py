from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sympy import sympify


def index(request):
    return render(request, 'main.html')


@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            result = str(counting(expression))
            return JsonResponse({'result': result})
        except (SyntaxError, TypeError, NameError):
            return JsonResponse({'error': 'Invalid expression'})


def counting(expression):
    expression = expression.replace('and', '&')
    expression = expression.replace('or', '|')
    expression = expression.replace('→', '>>')
    expression = expression.replace('⊕', '^')
    expression = expression.replace('≡', '==')

    try:
        result = sympify(expression)
        return result
    except (SyntaxError, TypeError, ValueError):
        return None
