from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    class Meta:
        model = Blog
        fields = ['id','title','content','slug','created_at','is_active','created_by']