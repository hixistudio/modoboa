
"""Modoboa - Mail hosting made simple."""

__version__ = "2.8.2"


def modoboa_admin():
    from modoboa.core.commands import handle_command_line

    handle_command_line()
