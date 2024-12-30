from django.db.models import Count, Max, Min, Q

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

#
from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer

#
#
# class PizzaListCreateView(APIView):
#     def get(self, request: Request, *args, **kwargs):
#         # pizzas = PizzaModel.objects.all()
#         # pizzas = PizzaModel.objects.filter(Q(price=180)| Q(name='Paperoni'))# якщо почали використовувати логічне або(Q) то його потрібно використовувати ло кінця і щоб добавити ще лоічне і потрібно &Q(...)
#         # pizzas = pizzas.filter(name='Paperoni')
#         # pizzas = PizzaModel.objects.filter(Q(price=180) | Q(name='Paperoni')).exclude(price=180).order_by('-price').reverse()# exclude-після відфільтрування виключає значення з пошуку по фільтру
#         # pizzas = PizzaModel.objects.all()[5:10:2]# зрізи в яких задаємо limit i offset при цьому objects.all не робить запит в БД бо це типу квері сет,але якщо вказати крок через 2 тоді робить запит
#         # aggregate = PizzaModel.objects.aggregate(Min('price'), Max('price'))
#         # annotate = PizzaModel.objects.values('name').annotate(count=Count('name'))
#         # print(annotate)
#         # pizzas = PizzaModel.objects.all().values('id', 'name')# можна витягувати не всі поля а вказати тільки які потрібно,але потрібно під це налаштувати serializer щоб він не вимагав інші поля
#         # serializer = PizzaSerializer(pizzas, many=True)
#         # return Response('ok')
#         qs = filter_pizza(request.query_params)
#         serializer = PizzaSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = PizzaSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         data = self.request.data
#         serializer = PizzaSerializer(pizza, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             PizzaModel.objects.get(pk=pk).delete()
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class PizzaListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get_queryset(self):
#         request: Request = self.request
#         return filter_pizza(request.query_params)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
# -------------------------------------------------------------------
# def get(self, request: Request, *args, **kwargs):
#     qs = filter_pizza(request.query_params)
#     serializer = PizzaSerializer(qs, many=True)
#     return Response(serializer.data, status.HTTP_200_OK)
#
# def post(self, *args, **kwargs):
#     data = self.request.data
#     serializer = PizzaSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status.HTTP_201_CREATED)


# class PizzaRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
# --------------------------------------------------------------------
# def get(self, *args, **kwargs):
#     pizza = self.get_object()
#     # pk = kwargs['pk']
#     #
#     # try:
#     #     pizza = PizzaModel.objects.get(pk=pk)
#     # except PizzaModel.DoesNotExist:
#     #     return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#     serializer = PizzaSerializer(pizza)
#     return Response(serializer.data, status.HTTP_200_OK)

# def put(self, *args, **kwargs):
# pizza = self.get_object()
# # pk = kwargs['pk']
# #
# # try:
# #     pizza = PizzaModel.objects.get(pk=pk)
# # except PizzaModel.DoesNotExist:
# #     return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#
# data = self.request.data
# serializer = PizzaSerializer(pizza, data=data, # partial=True(перевірятиме всі поля які йому передають так як написано в серіалайзері, але не вимагатиме повністю всіх полів)
# serializer.is_valid(raise_exception=True)
# serializer.save()
# return Response(serializer.data, status.HTTP_200_OK)

# def delete(self, *args, **kwargs):
# self.get_object().delete()
# # pk = kwargs['pk']
# #
# # try:
# #     PizzaModel.objects.get(pk=pk).delete()
# # except PizzaModel.DoesNotExist:
# #     return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#
# return Response(status=status.HTTP_204_NO_CONTENT)
class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    # pagination_class = None # можна відключати пагінацію для кожної views якщо не потрібно
    filterset_class = PizzaFilter

    # def get_queryset(self):
    #     request: Request = self.request
    #     return filter_pizza(request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer

    http_method_names = ['get', 'put', 'patch', 'delete']# дозволяє вибрати методи, наприклад можна виключити 'patch'
