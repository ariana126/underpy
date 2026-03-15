from assertpy import assert_that

from underpy import Fn


def dummy_function(_input: str) -> str:
    return _input


def dummy_function2(_input: str) -> str:
    return _input


class DummyClass:
    def __init__(self, _input: str) -> None:
        self._input = _input

    def dummy_function(self) -> str:
        return self._input

    def dummy_function2(self) -> str:
        return self._input


def test_callback_function_calls_the_original_function() -> None:
    _input = "dummy-value"
    expected_output = dummy_function(_input)
    sut = Fn(dummy_function, _input)

    output = sut.call()

    assert_that(output).is_equal_to(expected_output)

def test_callback_function_calls_the_original_function_in_a_class() -> None:
    _input = "dummy-value"
    cls = DummyClass(_input)
    expected_output = cls.dummy_function()
    sut = Fn(cls.dummy_function)

    output = sut.call()

    assert_that(output).is_equal_to(expected_output)

def test_callback_function_can_be_compared_to_the_original_function() -> None:
    sut = Fn(dummy_function)

    is_equal = sut.is_function(dummy_function)

    assert_that(is_equal).is_true()

def test_callback_function_is_not_equal_to_a_function_with_same_signature() -> None:
    sut = Fn(dummy_function)

    is_equal = sut.is_function(dummy_function2)

    assert_that(is_equal).is_false()

def test_callback_function_can_be_compared_to_the_original_function_in_a_class() -> None:
    cls = DummyClass('dummy-input')
    sut = Fn(cls.dummy_function)

    is_equal = sut.is_function(cls.dummy_function)

    assert_that(is_equal).is_true()

def test_callback_function_is_not_equal_to_a_function_with_same_signature_in_a_class() -> None:
    cls = DummyClass('dummy-input')
    sut = Fn(cls.dummy_function)

    is_equal = sut.is_function(cls.dummy_function2)

    assert_that(is_equal).is_false()

def test_callback_function_is_different_from_a_same_signature_function_in_a_class() -> None:
    cls = DummyClass('dummy-input')
    sut = Fn(dummy_function)

    is_equal = sut.is_function(cls.dummy_function)

    assert_that(is_equal).is_false()

def test_callback_function_in_a_object_considered_a_different_function() -> None:
    cls = DummyClass('dummy-input')
    cls2 = DummyClass('dummy-input-2')
    sut = Fn(cls.dummy_function)

    is_equal = sut.is_function(cls2.dummy_function)

    assert_that(is_equal).is_false()