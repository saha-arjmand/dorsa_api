from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import History, Total
from .serializers import HistorySerializer, TotalSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permissions import OnlyAdminCanSee
from rest_framework.throttling import UserRateThrottle

# The user should not be able to send more than 15 request responses
class WrongRequestsThrottle(UserRateThrottle):
    rate = '15/hour'


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')
    

class SumViewApi(APIView):
    """
        Sum two number : <br>
        Use Get method like this : GET /sum/?a=100&b=200 
    """

    throttle_classes = [WrongRequestsThrottle]

    # Users cannot send requests more than 100 times per hour. This value can be changed in the settings
    throttle_scope = 'sum'

    
    def get(self, request):
        # Django suggests us to use query_params instead of using GET directly
        a = request.query_params['a']
        b = request.query_params['b']

        try :
            a = int(a)
            b = int(b)
        except Exception as e:
            msg = str(e)
            return Response({"error": "The value entered is not valid", "error details":msg}, status=status.HTTP_400_BAD_REQUEST)
        
        result = a + b
        
        history_obj, created = History.objects.get_or_create(a = a, b = b)
        total_obj, created   = Total.objects.get_or_create(sum=history_obj)

        # This is to prevent data duplication
        if created == True:
            total_obj.total += result

        total_obj.save()
        
        return Response({"result": result}, status=status.HTTP_200_OK)
            
        

class HistoryViewApi(APIView):
    """
        Show a & b sent to the database : <br>
        Use Get method like this : GET /history/ 
    """

    # this add to code for swagger-ui documentation
    serializer_class = HistorySerializer

    throttle_classes = [WrongRequestsThrottle]

    # Authentication is required to view this view and check the user is admin for see this view
    authentication_classes = [TokenAuthentication]
    permission_classes =  [OnlyAdminCanSee]

    def get(self, request):
        history = History.objects.all()
        self.check_object_permissions(request, history)
        ser_history = HistorySerializer(instance=history, many=True)
        return Response(data=ser_history.data, status=status.HTTP_200_OK)



class TotalViewApi(APIView):
    """
        Show the history of total result : <br>
        Use Get method like this : GET /total/ 
    """

    # this add to code for swagger-ui documentation
    serializer_class = TotalSerializer
    
    throttle_classes = [WrongRequestsThrottle]

    # Authentication is required to view this view and check the user is admin for see this view
    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyAdminCanSee]

    def get(self, request):
        total = Total.objects.all()
        self.check_object_permissions(request, total)
        ser_total = TotalSerializer(instance=total, many=True)
        return Response(data=ser_total.data, status=status.HTTP_200_OK)