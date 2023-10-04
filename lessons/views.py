from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, IntegerField, F, ExpressionWrapper
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from .serializers import ViewDetailSerializer, ProductSerializer, ProductDetailSerializer
from .models import Product


# ------------Задание №1------------

class LessonsList(ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ViewDetailSerializer

    def get_queryset(self):
        return self.request.user.viewdetail_set.all()


# --------------Задание №2-----------------

#Выводит список продуктов, к которым у пользователя есть доступ
class ProductList(ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        data = self.request.user.products_joined.all()
        return data


class ProductDetail(ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ViewDetailSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return self.request.user.viewdetail_set.filter(lesson__product=pk)


# ---------------------Задание №3--------------------

class ProductStatistic(ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        users_all = User.objects.filter(is_staff=False).count()

        query = Product.objects.annotate(num_students=Count('users', distinct=True),
                                         sum_seconds=Sum('lessons__viewdetail__watched', distinct=True),
                                         people_watched=Count('lessons__viewdetail__status', distinct=True,
                                                              filter=Q(lessons__viewdetail__status='Просмотрено')),
                                         percent_buy=ExpressionWrapper(F('num_students') / users_all,
                                                                       output_field=IntegerField()))
        return query
