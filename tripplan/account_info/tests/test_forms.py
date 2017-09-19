from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from account_info.forms import ProfileForm, EmergencyContactForm, VehicleForm
from account_info.models import EmergencyContact

User = get_user_model()

'''
Testing checks that all fields are listed and labeled correctly. Future testing
will check that help text is displayed correctly
'''

class ProfileFormTests(TestCase):
    def test_full_name_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['full_name'].label, 'Full name')

    def test_preferred_name_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['preferred_name'].label, 'Preferred name')

    def test_primary_phone_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['primary_phone'].label, 'Phone (primary)')

    def test_secondary_phone_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['secondary_phone'].label, 'Phone (secondary)')

    def test_street_address_line_1_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['street_address_line1'].label, 'Address 1')

    def test_street_address_line_2_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['street_address_line2'].label, 'Address 2')

    def test_city_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['city'].label, 'City')

    def test_state_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['state'].label, 'State')

    def test_zip_code_field_label(self):
        form = ProfileForm()
        self.assertEqual(form.fields['zip_code'].label, 'ZIP code')

class EmergencyContactFormTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='valid@email.com',
            password='ValidPassword')

    def test_full_name_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['full_name'].label, '* Full name')

    def test_preferred_name_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['preferred_name'].label, 'Preferred name')

    def test_relationship_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['relationship'].label, '* Relationship')

    def test_primary_phone_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['primary_phone'].label, 'Phone (primary)')

    def test_secondary_phone_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['secondary_phone'].label, 'Phone (secondary)')

    def test_street_address_line_1_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['street_address_line1'].label, 'Address 1')

    def test_street_address_line_2_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['street_address_line2'].label, 'Address 2')

    def test_city_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['city'].label, 'City')

    def test_state_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['state'].label, 'State')

    def test_zip_code_field_label(self):
        form = EmergencyContactForm()
        self.assertEqual(form.fields['zip_code'].label, 'ZIP code')

    # def test_valid_data(self):
    #     ec = EmergencyContact.objects.create(full_name='Don Gately',
    #         relationship='Buddy', user = self.user)
    #     request = self.factory.post('/fake/')
    #     request.user = self.user
    #     form = EmergencyContactForm(request.POST, instance=ec)
    #     self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = EmergencyContactForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'full_name': ['This field is required.'],
            'relationship': ['This field is required.'],
            'user': ['This field is required.'],
        })

class VehicleFormTests(TestCase):
    def test_make_field_label(self):
        form = VehicleForm()
        self.assertEqual(form.fields['make'].label, '* Make')

    def test_model_field_label(self):
        form = VehicleForm()
        self.assertEqual(form.fields['model'].label, '* Model')

    def test_year_field_label(self):
        form = VehicleForm()
        self.assertEqual(form.fields['year'].label, 'Year')

    def test_color_field_label(self):
        form = VehicleForm()
        self.assertEqual(form.fields['color'].label, '* Color')

    def test_lic_plate_num_field_label(self):
        form = VehicleForm()
        self.assertEqual(form.fields['lic_plate_num'].label, '* License plate number')

    def test_lic_plate_st_field_label(self):
        form = VehicleForm()
        self.assertEqual(form.fields['lic_plate_st'].label, '* License plate state')