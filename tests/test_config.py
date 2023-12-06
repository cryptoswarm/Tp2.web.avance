# import os
# import unittest
# from flask import current_app
# from flask_testing import TestCase
# from src import create_app
# from config import config_by_name
# from config import BASE_DIR


# class TestDevelopmentConfig(TestCase):

#     def create_app(self):
#         app = create_app('dev')
#         app.config.from_object(config_by_name['dev'])
#         return app

#     def test_app_is_development(self):
#         with self.app.app_context:
#             self.assertFalse(self.app.config['SECRET_KEY'] is 'my_precious')
#             self.assertTrue(self.app.config['DEBUG'] is True)
#             self.assertFalse(current_app is None)
#             self.assertTrue(
#                 self.app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#             )


# class TestTestingConfig(TestCase):


#     def create_app(self):
#         app = create_app('test')
#         app.config.from_object(config_by_name['test'])
#         return app

#     def test_app_is_testing(self):
#         self.assertFalse(self.appapp.config['SECRET_KEY'] is 'my_precious')
#         self.assertTrue(self.appapp.config['DEBUG'])
#         self.assertTrue(
#             self.appapp.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(BASE_DIR, 'app_test.db')
#         )


# class TestProductionConfig(TestCase):

#     def create_app(self):
#         app = create_app('prod')
#         app.config.from_object(config_by_name['prod'])
#         return app

#     def test_app_is_production(self):
#         self.assertTrue(self.app.config['DEBUG'] is False)


# if __name__ == '__main__':
#     unittest.main()
