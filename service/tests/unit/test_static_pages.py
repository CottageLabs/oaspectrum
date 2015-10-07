from octopus.modules.es import testindex
from service.web import app

class TestStaticPages(testindex.ESTestCase):

    def setUp(self):
        super(TestStaticPages, self).setUp()

    def tearDown(self):
        super(TestStaticPages, self).tearDown()

    def test_01_static_pages(self):
        test_pages = ['/faq', '/sponsors', '/api']
        with app.test_client() as t_client:
            for url in test_pages:
                response = t_client.get(url)
                assert response.status_code == 200, response.status_code
                assert response.mimetype == 'text/html'