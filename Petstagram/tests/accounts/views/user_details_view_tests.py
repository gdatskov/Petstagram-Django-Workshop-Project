"""
1. User is owner
2. User is not owner
3. User has no pets
4. User has pets, no photos
5. User has pets, 1 photo
6. User has pets, 2 photos
7. User has pets, 7 photos, page = default
8. User has pets, 7 photos, page = 1
9. User has pets, 7 photos, page = 3

10. User has no likes
11. User has likes for 1 pet
12. User has likes for multiple pets
"""
from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()



class UserDetailsViewTests(TestCase):

    VALID_USER_DATA = {
        'username': 'valid_username',
        'password': 'OPIG*H*)&FH@#$89fguwnrefgvj',
        # 'password1': 'OPIG*H*)&FH@#$89fguwnrefgvj',
        # 'password2': 'OPIG*H*)&FH@#$89fguwnrefgvj',
        'email': 'test@test.test'
    }

    # 1
    def test_user_details__when_owner__expect_its_owner(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)

    # 2
    def test_user_details__when_not_owner__expect_its_not_owner(self):
        pass

    # 3
    def test_user_details__when_user_has_no_pets__expect_no_pets(self):
        pass

    # 4
    def test_user_details__when_user_has_pets_but_no_photos__expect_pets_no_photos(self):
        pass

    # 5
    def test_user_details__when_user_has_pets_and_1_photo__expect_pets_and_1_photo(self):
        pass

    # 6
    def test_user_details__when_user_has_pets_and_2_photos__expect_pets_and_2_photos(self):
        pass


    # 7
    def test_user_details__when_user_has_pets_and_7_photos_no_page__expect_pets_and_7_photos(self):
        pass

    #8
    def test_user_details__when_user_has_pets_and_7_photos_1st_page__expect_pets_and_7_photos(self):
        pass

    #9
    def test_user_details__when_user_has_pets_and_7_photos_2nd_page__expect_pets_and_7_photos(self):
        pass

    #10
    def test_user_details__when_no_likes__expect_0_likes_count(self):
        pass

    #11
    def test_user_details__when_like_for_1_pet__expect_correct_likes_count(self):
        pass

    #12
    def test_user_details__when_like_for_multiple_pets__expect_correct_combined_likes_count(self):
        pass



