from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from products.models import Contact, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ['created', ]

    def save(self):

        if self._validated_data['subject'] is None:
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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image', 'price_currency', 'price', 'is_active', 'in_stock', ]
