from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
import pytz
from .serializers import InfoSerializer  


class InfoAPIView(APIView):
    def get(self, request):
        slack_name = request.query_params.get('slack_name')
        track = request.query_params.get('track')

        if not slack_name or not track:
            return Response(
                {"error": "Both slack_name and track parameters are required."},
                status=400
            )
        

  
        
        current_day = datetime.now(pytz.utc).strftime('%A')
        # utc_now = datetime.now(pytz.utc)
        # utc_now = datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        utc_now = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")



        # Calculate the UTC time within a +/-2 minute window
        # utc_time = utc_now + timedelta(minutes=2)  # Add 2 minutes
        # utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        

        github_repo_url = "https://github.com/breezeconcept/HNGx_Task1"
        github_file_url = f"{github_repo_url}/blob/main/home/views.py"

        data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_now,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200,
        }

        serializer = InfoSerializer(data)
        return Response(serializer.data)
