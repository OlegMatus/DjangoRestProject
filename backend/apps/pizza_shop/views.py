from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.pizza.serializers import PizzaSerializer
from apps.pizza_shop.models import PizzaShopModel
from apps.pizza_shop.serializer import PizzaShopSerializer


class PizzaShopListCreateView(ListCreateAPIView):
    serializer_class = PizzaShopSerializer
    queryset = PizzaShopModel.objects.all()

class PizzaShopAddPizzaView(GenericAPIView):
    queryset = PizzaShopModel.objects.all()

    def post(self,*args,**kwargs):
        pizza_shop = self.get_object()
        data = self.request.data
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pizza_shop=pizza_shop)
        shop_serializer = PizzaShopSerializer(pizza_shop)
        return Response(shop_serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        pizza_shop = self.get_object()
        pk = kwargs['pk']

        try:
             pizza_shop = PizzaShopModel.objects.get(pk=pk)
        except PizzaShopModel.DoesNotExist:
             return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PizzaShopSerializer(pizza_shop)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self,*args,**kwargs):
        pk = self.kwargs['pk']
        try:
            PizzaShopModel.objects.get(pk=pk).delete()
        except PizzaShopModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
