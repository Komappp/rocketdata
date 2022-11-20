from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Company, Product
from .permissions import IsActive
from .serializers import CompanySerializer, ProductSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [IsActive, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'products']

    @action(detail=False, url_path='big_debt')
    def get_big_debt_creditors(self, request):
        '''Returns list companies whose debt bigger then average'''
        avg = Company.objects.aggregate(Avg('debt'))['debt__avg']
        queryset = Company.objects.filter(debt__gt=avg)
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
