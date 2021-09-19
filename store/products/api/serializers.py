from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from products.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ['created', ]

    def save(self):

        if self._validated_data['name'] is None:
            raise serializers.ValidationError({
                'name': _('Please enter your name'),
            })

        elif self._validated_data['email'] is None:
            raise serializers.ValidationError({
                'email': _('Please enter your email.')
            })

        elif self._validated_data['subject'] is None:
            raise serializers.ValidationError({
                'subject': _('Please enter a subject.')
            })

        elif self._validated_data['message'] is None:
            raise serializers.ValidationError({
                'message': _('Please enter a message.')
            })

        new_contact = Contact(
            name=self._validated_data['name'],
            email=self._validated_data['email'],
            subject=self._validated_data['subject'],
            message=self._validated_data['message'],
        )
        new_contact.save()
        return new_contact
