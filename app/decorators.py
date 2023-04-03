from .model import Permission
from functools import wraps
from flask_login import current_user
from flask import abort


def authority(permissions):
    def decorator(f):
        @wraps(f)
        def inner_decorator(*args, **kwargs):
            if not current_user.can(permissions):
                abort(403)
            return f(*args, **kwargs)
        return inner_decorator
    return decorator


def is_admin(f):
    return authority(Permission.ADMINISTER)(f)


def is_counsellor(f):
    return authority(Permission.COUNSELLOR)(f)


def is_user(f):
    return authority(3)(f)
