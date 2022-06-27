from asyncio.windows_events import NULL
import django
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializer import ContactSerializer
from rest_framework import status
from django.forms.models import model_to_dict

class ContactView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            contact_data = Contact.objects.filter(id=pk).first()
            serialized_data = ContactSerializer(data=contact_data)
            return Response({"message": "Success","data": model_to_dict(contact_data)}, status=status.HTTP_200_OK)
        else:
            contact_data = Contact.objects.all()
            serialized_data = ContactSerializer(contact_data, many=True)
            return Response({"message": "Success","data": serialized_data.data}, status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        contact_data = Contact.objects.create(**request.data)
        return Response({"message": "Success","data": model_to_dict(contact_data)}, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        update_status = Contact.objects.filter(
                id=pk).update(**request.data)
        if update_status:
            return Response({"message": "Success","data": model_to_dict(Contact.objects.filter(id=pk).first())}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Failure","data": "Update failed"}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk):
        contact_data = Contact.objects.get(id=pk).delete()
        return Response({"message": "Success", "data": None}, status=status.HTTP_200_OK)
