from django.urls import path, include
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from rest_framework import routers, serializers, viewsets
from quiz.models import  Category, Question, Badge, Player, Statistics
from django.contrib.auth.models import User



router = routers.DefaultRouter()

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        depth = 1


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Routers provide an easy way of automatically determining the URL conf.

router.register(r'categories', CategoryViewSet)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.CharField(write_only=True)
    class Meta:
        model = Question
        fields = '__all__'
        depth = 1


# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Routers provide an easy way of automatically determining the URL conf.

router.register(r'questions', QuestionViewSet, )


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'


# ViewSets define the view behavior.
class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


# Routers provide an easy way of automatically determining the URL conf.

router.register(r'badges', BadgeViewSet, )



class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    badge_id = serializers.CharField(write_only=True)
    class Meta:
        model = Player
        fields = '__all__'
        depth = 1


# ViewSets define the view behavior.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


# Routers provide an easy way of automatically determining the URL conf.

router.register(r'players', PlayerViewSet, )


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


# ViewSets define the view behavior.
class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer


# Routers provide an easy way of automatically determining the URL conf.

router.register(r'statistics', StatisticsViewSet, )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.

router.register(r'users', UserViewSet)


urlpatterns = [
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]