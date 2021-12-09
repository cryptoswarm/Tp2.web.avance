# import os
# import unittest
# from flask import current_app
# from flask_testing import TestCase

# import inf5190_projet_src
# # from TP2.we inf5190_projet_src import create_app
# from . import inf5190_projet_src
# from config import BASE_DIR


# class TestDevelopmentConfig(TestCase):

#     # def create_app(self):
#     #     app.config.from_object('config.DevelopmentConfig')
#     #     return app
#     app = inf5190_projet_src.create_app('dev')

#     def test_app_is_development(self):
#         with self.app.app_context:
#             self.assertFalse(self.app.config['SECRET_KEY'] is 'my_precious')
#             self.assertTrue(self.app.config['DEBUG'] is True)
#             self.assertFalse(current_app is None)
#             self.assertTrue(
#                 self.app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#             )


# class TestTestingConfig(TestCase):

#     app = inf5190_projet_src.create_app('test')
    
#     # def create_app(self):
#     #     self.app.config.from_object('config.TestingConfig')
#     #     return self.app

#     def test_app_is_testing(self):
#         self.assertFalse(self.appapp.config['SECRET_KEY'] is 'my_precious')
#         self.assertTrue(self.appapp.config['DEBUG'])
#         self.assertTrue(
#             self.appapp.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(BASE_DIR, 'app_test.db')
#         )


# class TestProductionConfig(TestCase):

#     # def create_app(self):
#     #     app.config.from_object('config.ProductionConfig')
#     #     return app
#     app = inf5190_projet_src.create_app('test')
    
#     def test_app_is_production(self):
#         self.assertTrue(self.app.config['DEBUG'] is False)


# if __name__ == '__main__':
#     unittest.main()