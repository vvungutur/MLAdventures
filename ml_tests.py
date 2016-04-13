import unittest

import ml


class MlTestCase(unittest.TestCase):
    def setUp(self):
        ml.app.config['TESTING'] = True
        self.app = ml.app.test_client()

    def tearDown(self):
        pass

    def test_base_route(self):
        assert self.app.get('/')


if __name__ == '__main__':
    unittest.main()
