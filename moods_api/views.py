# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .classifier import text_classify

@api_view(['GET', 'POST'])

def process_input(request):
    if(request.method == 'GET'):
        return Response({'message': 'testing...testing... yall.'})
    
    user_input = request.data.get('text', '')
 

    if not user_input:
        return Response({'error': 'No input provided'}, status=400)

    #model
    raw_result = text_classify(user_input)
    if raw_result and isinstance(raw_result, list) and isinstance(raw_result[0], list):
        result = max(raw_result[0], key=lambda x: x['score']) ['label']

    else:
        result = 'unknown'

    return Response({'prediction': result})

