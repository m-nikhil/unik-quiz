from rest_framework import generics, renderers
from rest_framework.response import Response
from . import models
from . import serializers


class QuizList(generics.ListAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.PostSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    
    def get(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        return Response({'quizz': self.queryset}, template_name='api/quiz.html')


# class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Quiz.objects.all()
#     serializer_class = serializers.PostSerializer