from rest_framework import serializers

from entries.models import(Entry,TestString,User)
class EntrySerializer(serializers.ModelSerializer):


    test_strings=serializers.SlugRelatedField(
        querySet=TestString.object.all(),
        many=True,
        slug_fields='string',
        
    )
    user=serializers.SlugRelatedField(
        queryset=User.object.all(),
        slug_field='username',
    )
    class Meta:
        model=Entry
        fields=[
            'date_added',
            'id',
            'pattern',
        ]
        