# underpy 🐍

**Reusable Python base classes for clean, maintainable, and scalable projects.**  
Underpy provides foundational building blocks such as encapsulated data, immutable objects, service patterns, and JSON typing — so you can start every new project with a solid, consistent architecture.

---

## ✨ Features

- **Encapsulated** – Hide internals and expose clean public APIs
- **Immutable** – Prevent changes to objects after initialization
- **Service Class (Singleton)** – Enforce a single point of access for core services
- **JSON Type** – Typed JSON data handling made easy
- **Tested with Pytest + AssertPy** – Reliable and expressive tests

---

## 📦 Installation

Install from source:

```bash
pip install git+https://github.com/ariana126/underpy.git
```
or PyPI
```bash
pip install underpyx
```

---

## 🚀 Quick Start

### Example: Encapsulated
```python
from underpy import Encapsulated

class User(Encapsulated):
    def __init__(self, username):
        self._username = username

    def get_username(self):
        return self._username

user = User("ariana")
print(user.get_username())  # ✅ "ariana"
# Direct access is avoided: user._username
```

---

### Example: Immutable
```python
from underpy import Immutable

class Config(Immutable):
    def __init__(self, host, port):
        self.host = host
        self.port = port

cfg = Config("localhost", 8080)
# cfg.port = 9000  # ❌ Raises AttributeError
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📄 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Contributions are welcome!  
If you have an improvement or find a bug:
1. Fork the repo
2. Create your branch
3. Submit a pull request

---

## 🤖 Agent Skill

An [agentskills.io](https://agentskills.io)-compatible skill is available so AI coding agents (like Claude Code) automatically know how to use this package.

Copy `docs/agents/skills/underpy/` into your Claude skills directory:

```bash
mkdir -p ~/.claude/skills
cp -r docs/agents/skills/underpy ~/.claude/skills/
```

Once installed, agents will automatically recognize when you're using `underpy` and apply correct usage patterns for `Encapsulated`, `Immutable`, `ServiceClass`, `JSON`, and `Fn`.

---

## 💡 About
This project is part of a personal utility toolkit used to maintain a consistent, clean architecture across Python projects.  
Originally authored by [Ariana](https://github.com/ariana126).