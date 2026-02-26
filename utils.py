from functools import wraps
from datetime import datetime


def track_access(func):
    """
    Decorator to log access to borrow and return book methods.
    Logs method name, arguments, and timestamp.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"[LOG] Method: {func.__name__}")
        print(f"[LOG] Args: {args[1:]}, Kwargs: {kwargs}")
        print(f"[LOG] Accessed at: {timestamp}")
        return func(*args, **kwargs)

    return wrapper


def permission_check(required_role):
    """
    Closure that returns a decorator to enforce role-based permissions.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(self, user, *args, **kwargs):
            if getattr(user, "role", None) != required_role:
                raise PermissionError(
                    f"Access denied. {required_role} role required."
                )
            return func(self, user, *args, **kwargs)

        return wrapper

    return decorator