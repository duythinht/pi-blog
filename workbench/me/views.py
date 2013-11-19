from django.views.generic.list import ListView
from models import Track


class TrackView(ListView):
    model = Track
    paginate_by = 20