import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer


client = Client()


class GetAllPuppiesTest(TestCase):
    def setUp(self):
        Puppy.objects.create(name="Muffin", age=3, breed="Poodle", color="Brown")
        Puppy.objects.create(name="Bear", age=1, breed="Husky", color="Black")
        Puppy.objects.create(name="Rover", age=4, breed="Labrador", color="White")
    
    def test_get_all_puppies(self):
        response = client.get(reverse('get_post_puppies'))
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': 1})
        )
        puppy = Puppy.objects.get(pk=1)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPuppyTest(TestCase):
    """ Test module for insert a new puppy """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Poodle',
            'color': 'Brown'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Poodle',
            'color': 'Brown'
        }
    
    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.valid_payload), #o que é o json.dumps? metodo que converte um dicionario em json
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = Puppy.objects.create(
            name='Casper', age=4, breed='Bull Dog', color='Black'
        )
        self.muffin = Puppy.objects.create(
            name='Muffy', age=3, breed='Poodle', color='Brown'
        )
        self.valid_payload = {
            'name': 'Muffy',
            'age': 4,
            'breed': 'Poodle',
            'color': 'Brown'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Poodle',
            'color': 'Brown'
        }

        def test_valid_update_puppy(self):
            response = client.put(
                reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
                data=json.dumps(self.valid_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        def test_invalid_update_puppy(self):
            response = client.put(
                reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
                data=json.dumps(self.invalid_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = Puppy.objects.create(
            name='Casper', age=4, breed='Bull Dog', color='Black'
        )
        self.muffy = Puppy.objects.create(
            name='Muffy', age=3, breed='Poodle', color='Brown'
        )

    def test_valid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffy.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_puppy', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

