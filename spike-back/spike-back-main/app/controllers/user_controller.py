"""Implementation for controlling the user data."""
import bcrypt

from app.config import fb_db

__all__ = ('UserController',)


class UserController:
    """User data controller."""

    @staticmethod
    def create_user(user):
        """Create a new user data."""
        new_user = {
            'username': user.username,
            'password': user.password,
            'phone': user.phone,
            'address': user.address,
            'type': user.type,
            'email': user.email,
        }

        fb_db.collection('Users').document(user.username).set(new_user)

        return user.username

    @staticmethod
    def get_user(username):
        """Get the user data of ``user_name``."""
        user = fb_db.collection('Users').document(username).get()

        user_dic = user.to_dict()
        del user_dic['password']
        return user_dic

    @classmethod
    def update_user(cls, username, properties):
        """Update the ``properties`` of the user data ``username``."""
        doc_ref = fb_db.collection('Users')
        doc = doc_ref.document(username)

        keys = properties.keys()

        if 'password' in keys:
            password = properties['password'].encode('utf8')
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            properties['password'] = hashed
        if 'username' in keys:
            del properties['username']
        doc.update(properties)
        user = cls.get_user(username)
        return user

    @staticmethod
    def delete_user(username):
        """Delete the user at ``username``."""
        fb_db.collection('Users').document(username).delete()
        return username
