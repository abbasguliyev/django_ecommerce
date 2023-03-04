from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model

def user_list() -> QuerySet[get_user_model()]:
    qs = get_user_model().objects.prefetch_related("groups", "user_permissions").all()
    return qs
