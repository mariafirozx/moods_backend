# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .classifier import text_classify

@api_view(['GET', 'POST'])

def process_input(request):
    if(request.method == 'GET'):
        return Response({'message': 'testing...testing... yall.'})
    
    user_input = request.data.get('text', '').strip()
 

    if not user_input:
        return Response({'error': 'No input provided'}, status=400)

    #model
    unfilteredRes = text_classify(user_input)
    print("raw results", unfilteredRes)


    if isinstance(unfilteredRes, list):
        curr = unfilteredRes[0] if isinstance(unfilteredRes[0],list) else unfilteredRes 
        result = max(curr, key=lambda x: x['score'])['label']

    else:
        result = "unknown"

    # if raw_result and isinstance(raw_result, list) and isinstance(raw_result[0], list):
    #     result = max(raw_result[0], key=lambda x: x['score']) ['label']

    # else:
    #     result = 'unknown'

    return Response({'prediction': result})

