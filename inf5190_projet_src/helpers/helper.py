import functools
from flask import g
from flask import redirect, url_for

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("user.login"))

        return view(**kwargs)

    return wrapped_view