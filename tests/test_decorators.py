import pytest

from src.decorators import log


@pytest.fixture
def log_file_path(tmp_path):
    """Временный файл для логов при filename != None."""
    return tmp_path / "app.log"


def test_log_success_writes_to_file(log_file_path):
    @log(filename=str(log_file_path))
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3

    with open(log_file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    assert len(lines) == 2
    assert "НАЧАЛО выполнения функции 'add' с аргументами: 1, 2" in lines[0]
    assert "УСПЕХ: функция 'add' завершилась. Результат: 3" in lines[1]


def test_log_error_writes_error_and_traceback_to_file(log_file_path):
    @log(filename=str(log_file_path))
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    with open(log_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "ОШИБКА в функции 'div':" in content
    assert "Тип ошибки: ZeroDivisionError" in content
    assert "Аргументы: 1, 0" in content
    # traceback добавляет несколько строк
    assert content.count("\n") >= 3


def test_log_with_kwargs_formats_signature_correctly(log_file_path):
    @log(filename=str(log_file_path))
    def func(x, y, z=10):
        return x + y + z

    func(1, 2, z=3)

    with open(log_file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    assert len(lines) == 2
    assert "с аргументами: 1, 2, z=3" in lines[0]
    assert "Результат: 6" in lines[1]


def test_log_without_filename_uses_stdout_via_capsys(capsys):
    @log()  # без filename → вывод в stdout
    def say(msg):
        return msg

    say("hello")

    out, err = capsys.readouterr()
    assert "НАЧАЛО выполнения функции 'say' с аргументами: hello" in out
    assert "УСПЕХ: функция 'say' завершилась. Результат: 'hello'" in out
    assert err == ""


def test_log_error_without_filename_prints_error_via_capsys(capsys):
    @log()
    def bad():
        raise ValueError("test error")

    with pytest.raises(ValueError, match="test error"):
        bad()

    out, err = capsys.readouterr()
    assert "ОШИБКА в функции 'bad':" in out
    assert "Тип ошибки: ValueError" in out
    assert "Сообщение: test error" in out
    # traceback печатается в stderr
    assert "ValueError: test error" in err


def test_log_preserves_function_metadata(log_file_path):
    @log(filename=str(log_file_path))
    def secret(x):
        """Secret docstring."""
        return x * 2

    assert secret.__name__ == "secret"
    assert secret.__doc__ == "Secret docstring."


def test_log_does_not_swallow_exceptions(log_file_path):
    @log(filename=str(log_file_path))
    def boom():
        raise RuntimeError("boom!")

    with pytest.raises(RuntimeError, match="boom!"):
        boom()

    with open(log_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "ОШИБКА в функции 'boom':" in content
    assert "Тип ошибки: RuntimeError" in content
