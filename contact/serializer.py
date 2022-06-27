from rest_framework.serializers import ModelSerializer
from .models import Contact
import phonenumbers


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
    """
    def validate(self, data):
        if (phonenumbers.is_possible_number(phonenumbers.parse(data['phone_number'])))==False:
            raise ModelSerializer.ValidationError("Invalid phone number")
        return super().validate(data)
    """