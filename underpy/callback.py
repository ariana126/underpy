from typing import Callable, ParamSpec, TypeVar

from . import Immutable, Encapsulated

P = ParamSpec("P")
R = TypeVar("R")
class Fn(Encapsulated, Immutable):
    def __init__(self, callback: Callable[P, R], *callback_args: P.args, **callback_kwargs: P.kwargs):
        self.__callback = callback
        self.__callback_args = callback_args
        self.__callback_kwargs = callback_kwargs

    def call(self) -> R:
        return self.__callback(*self.__callback_args, **self.__callback_kwargs)

    def is_function(self, function: Callable[P, R]) -> bool:
        if hasattr(self.__callback, "__func__") and hasattr(function, "__func__"):
            return (getattr(self.__callback, "__func__") is getattr(function, "__func__") and
                    getattr(self.__callback, "__self__") is getattr(function, "__self__"))
        return self.__callback is function