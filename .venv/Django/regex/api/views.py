from rest_framework import viewsets
from api.serializers import EntrySerializer
from rest_framework import permissions
from entries.models import Entry
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.object.all().order_by('-date_added')
    serializer_class=EntrySerializer
    permission_classes=[permissions.IsAuthenticated]



# Create your views here.
