from rest_framework import serializers
from .models import CustomUser, Contact, Achievements, About, Question, Gallery


class QuestionFormSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    question = serializers.CharField(required=False)
    class Meta:
        model = Question
        fields = ['name', 'question']

    def validate(self, data):
        if not data.get('question'):
            raise serializers.ValidationError("Savol maydoni bo'sh bo'lishi mumkin emas!")
        if not data.get('name'):
            raise serializers.ValidationError("Ism maydoni bo'sh bo'lishi mumkin emas!")
        return data

    def create(self, validated_data):
        return Question.objects.create(**validated_data)


class QuestionListSerializer(serializers.ModelSerializer):
    answered_by = serializers.CharField(source='answered_by.get_full_name', read_only=True)
    class Meta:
        model = Question
        fields = ['id','name','question','created_at','is_active','answered_at','answered_by']

class QuestionDetailSerializer(serializers.ModelSerializer):
    answered_by = serializers.CharField(source='answered_by.get_full_name', read_only=True)
    class Meta:
        model = Question
        fields = ['id','name','question','created_at','is_active','answered_at','answered_by']

class ContactSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    class Meta:
        model = Contact
        fields = ['id','title','social_account_name','social_account_link','created_at','is_active','created_by']

class AboutSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    class Meta:
        model = About
        fields = ['id','title','description','created_at','created_by','is_active','updated_at']



class AchievementsSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    class Meta:
        model = Achievements
        fields = ['id','title','description','image','created_at','created_by','is_active']


class GallerySerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    class Meta:
        model = Gallery
        fields = ['id','title','image','created_at','created_by','is_active']