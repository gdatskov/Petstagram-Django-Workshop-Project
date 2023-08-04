from petstagram.pets.models import Pet


def get_pet_by_slug_and_username(slug, username):
    objects = Pet.objects \
        .filter(pet_slug=slug, pet_user__username=username) \
        .get()
    return objects


# Anti-URL-tampering (function-based-views)
def is_owner(request, user):
    return request.user == user


# Anti-URL-tampering (class-based-views)
class OwnerRequired:
    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)

        if request.user == self.object.user:
            return result
        else:
            return ...  # Defence URL

    # def post(self):
    # same logic

    # def other CRUD...
