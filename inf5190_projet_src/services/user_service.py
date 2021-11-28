# import uuid
# import hashlib
# from inf5190_projet_src.repositories.user_repo import *
# from werkzeug.security import generate_password_hash, check_password_hash


# def register_new_user(data):

#     if validation_rs.flag:
#         print('username : ',data['username'])
#         user = filter_by_username(data['username'])
#         user_by_email = filter_by_email(data['email'])
#         if user is None:
#             if user_by_email is not None:
#                 return Response('email already taken', False, None, 400)
#             salt = uuid.uuid4().hex
#             #hashlib.sha512(str(data['password'] + salt).encode("utf-8")).hexdigest()
#             hashed_pass = generate_hashed_pass(data['password'], salt).encode("utf-8")
#             new_user = User(data['email'], data['username'], hashed_pass, salt)
#             #print('user to be created :',new_user)
#             user_id = save_user(new_user)
#             return Response('Created', True, user_id, 201)
#         return Response('username already taken', False, None, 400)
#     return validation_rs


# def generate_hashed_pass(plain_text_pass, salt):
#     to_be_hash = str(plain_text_pass + salt)
#     print('to be hashed is :', to_be_hash)
#     hash = generate_password_hash(to_be_hash)
#     print('hash is :',hash)
#     return hash


# def find_existing_user(data):
#     print('received data :',data)
#     username = data["username"]
#     print('username received :',username)
#     plain_text_pass = data["password"]
#     #secret = str(username + plain_text_pass)
#     secret = None
    
#     existing_user = filter_by_username(username)
#     #secret = str(plain_text_pass + existing_user.salt)
#     if existing_user is not None:
#         secret = str(plain_text_pass + existing_user.salt)
#     else:
#         return Response("Incorrect username.", False, None, 400)
#     if check_password_hash(existing_user.hashed_pass.decode("utf-8") , secret) is False:
#         print('user services --> Incorrect password')
#         return Response("Incorrect password.", False, None, 400)
#     return Response('', True, existing_user.id, 200)

# def find_existing_user_by_id(id):
#     existing_user = filter_by_id(id)
#     return existing_user