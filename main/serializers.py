from rest_framework import serializers
from .models import CustomUser , Contact , Achievements , About , Question





class QuestionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['name','question']
        def validate(self,data):
            if not data['question']:
                raise serializers.ValidationError("Savol maydoni bo'sh bo'lishi mumkin emas!")
            elif not data['name']:
                raise serializers.ValidationError("Ism maydoni bo'sh bo'lishi mumkin emas!")
            return data
        def create(self, validated_data):
            return Question.objects.create(**validated_data)



