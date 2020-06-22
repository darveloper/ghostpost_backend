from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'text',
            'created_at',
            'upvotes',
            'downvotes',
            'total_votes',
            'is_boast'
            )