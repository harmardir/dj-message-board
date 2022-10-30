from django.test import TestCase
from django.urls import reverse
from .models import Post


'''
this test will add sample post to the text database field and then check that is is stored
correctly in the database
TestCase module lets us create a sample database and our Post model
setUp method will create a new database that has one entry: a post with a text filed containing
the string 'just a test'
then we run our first test : test_text_content to check that the database field actually contains
just a test.
we created a variable called post that represents the first id on our Post model
'''
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')
    
    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')
'''
The next group of tests is to evaluate the homepage:
1- does it actualy exists and return HTTP 200 response ?
2- does it use HomePageView as the view ?
3- does it use home.html as the template ?
we used reverse to refer to the named URL of home , becausae URL schemes can and do change
over the course of a project, but name URL likely will not
'''

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


