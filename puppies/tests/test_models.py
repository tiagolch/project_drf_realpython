from django.test import TestCase
from ..models import Puppy


class PuppyTest(TestCase):
    """
        Test module for Puppy model
    """

    def setUp(self):
        Puppy.objects.create(
            name='Muffin',
            age=3,
            breed='Poodle',
            color='Brown'
        )
        Puppy.objects.create(
            name='Maya',
            age=4,
            breed='Yorkie',
            color='Gray'
        )

    def test_puppy_bread(self):
        """ Test Puppy breed """
        puppy_muffin = Puppy.objects.get(name='Muffin')
        puppy_maya = Puppy.objects.get(name='Maya')
        
        self.assertEqual(puppy_muffin.get_breed(), 'Muffin is a Poodle')
        self.assertEqual(puppy_maya.get_breed(), 'Maya is a Yorkie')
