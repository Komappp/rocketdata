from rest_framework import serializers

from .models import Company, Product


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, data):
        instance = self.instance
        if instance is not None:
            original_debt = instance.debt
            new_debt = data.get('debt')
            # Если кто нибудь решил изменить задолженность через API
            # просто изменим входящие данные на оригинал
            if new_debt is not None and (new_debt != original_debt):
                data.update({'debt': original_debt})
        return data


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'