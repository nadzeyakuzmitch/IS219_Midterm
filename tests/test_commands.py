"""Commands testing module"""
import pytest
from app import App

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['add', '2', '3', 'add', 'f', '2', 'add', 'stop', 'add', '2', 'stop', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['subtract', '2', '3', 'subtract', 'f', '2', 'subtract', 'stop', 'subtract', '2', 'stop', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['multiply', '2', '3', 'multiply', 'f', '2', 'multiply', 'stop', 'multiply', '2', 'stop', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['divide', '2', '3', 'divide', 'f', '2', 'divide', 'stop', 'divide', '2', 'stop', 'divide', '2', '0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"
