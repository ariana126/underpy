# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run a single test file
pytest tests/unit/test_encapsulated.py

# Run a single test
pytest tests/unit/test_encapsulated.py::TestEncapsulated::test_name

# Build the package
python -m build

# Publish to PyPI
twine upload dist/*
```

## Architecture

**underpy** (PyPI: `underpyx`) is a pure-Python utility library with zero runtime dependencies. It provides abstract base classes (ABCs) that enforce stricter OOP guarantees — encapsulation, immutability — which Python doesn't enforce natively.

The five exported names from `underpy/__init__.py`:

| Export | Module | Purpose |
|---|---|---|
| `Encapsulated` | `encapsulation.py` | ABC that enforces access control (`_protected`, `__private`) at runtime via `inspect.currentframe()` |
| `Immutable` | `mutability.py` | ABC + metaclass that freezes all attributes after `__init__` completes |
| `ServiceClass` | `service.py` | Thin composite of `Encapsulated + Immutable + ABC` for service-layer objects |
| `JSON` | `typing.py` | Recursive `Union` type alias for arbitrary JSON-structured data |
| `Fn` | `callback.py` | Immutable, encapsulated callable wrapper with `call()` and `is_function()` |

### Key design details

- **`Encapsulated`** uses `__getattribute__` / `__setattr__` hooks + `inspect.currentframe()` to check the call stack and raise `AttributeError` for access violations. Name-mangling (`__attr` → `_Class__attr`) assists but is supplemented by runtime checks.
- **`Immutable`** works via `ImmutableMeta` metaclass: sets `_initialized = True` on the instance *after* `__init__` returns; subsequent `__setattr__` / `__delattr__` calls raise `AttributeError`.
- **`ServiceClass`** is just 3 lines — all logic is in the parent classes.
- **`Fn`** uses `ParamSpec` + `TypeVar` for generic type safety on wrapped callables. Its `is_function()` handles bound methods by comparing both `__func__` and `__self__`.

### Known design gaps (see `TODO` comments)
- `_check_` methods and `_initialized` internal attributes are currently accessible as protected rather than truly private.

## Testing conventions

- Tests live in `tests/unit/`, one file per module.
- Test subjects are named `sut` ("System Under Test").
- Uses `assertpy` fluent assertions: `assert_that(value).is_equal_to(...)`.
- Exception cases use `pytest.raises(AttributeError)`.
- Test bodies follow explicit Arrange / Act / Assert sections.

## Release process

- Package name on PyPI is `underpyx`; import name is `underpy`.
- Requires Python ≥ 3.10 (uses `ParamSpec`).
- Commit messages follow Conventional Commits: `feat:`, `fix:`, `doc:`, `chore:`, `build:`.
- Publishing is automated via `.github/workflows/publish-to-pypi.yml` — triggered by creating a GitHub release, uses `PYPI_API_TOKEN` secret.
