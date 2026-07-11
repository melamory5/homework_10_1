import functools
import traceback
from datetime import datetime


def log(filename=None):
    """
    Декоратор для логирования начала и конца выполнения функции,
    а также результатов или ошибок.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_ = [str(a) for a in args]
            kwargs_ = [f"{k}={str(v)}" for k, v in kwargs.items()]
            signature = ", ".join(args_ + kwargs_)

            start_message = (
                f"[{datetime.now().isoformat()}] НАЧАЛО выполнения функции "
                f"'{func.__name__}' с аргументами: {signature}"
            )

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(start_message + "\n")
            else:
                print(start_message)

            try:
                result = func(*args, **kwargs)

                end_message = (
                    f"[{datetime.now().isoformat()}] УСПЕХ: функция "
                    f"'{func.__name__}' завершилась. Результат: {result!r}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(end_message + "\n")
                else:
                    print(end_message)

                return result

            except Exception as e:
                error_message = (
                    f"[{datetime.now().isoformat()}] ОШИБКА в функции '{func.__name__}': "
                    f"Тип ошибки: {type(e).__name__}, "
                    f"Сообщение: {str(e)}, "
                    f"Аргументы: {signature}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                        f.write(traceback.format_exc() + "\n")
                else:
                    print(error_message)
                    traceback.print_exc()

                raise

        return wrapper

    return decorator
