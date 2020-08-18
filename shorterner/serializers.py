from rest_framework import serializers
from shorterner.models import shorturl


class shorturlSerializers(serializers.ModelSerializer):
    class Meta:
        model=shorturl
        fields = ('id',
                  'url',
                  'shortcode')