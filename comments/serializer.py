from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_by')

# class ProfileSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True)
#
#     class Meta:
#         model = Profile
#         fields = '__all__'