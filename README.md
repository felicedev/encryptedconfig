# encryptedconfig

`encryptedconfig` is a Python package for managing encrypted configuration files across multiple formats (`.ini`, `.json`, `.yaml`, `.properties`, and `.txt`). It supports easy encryption and decryption with a focus on developer simplicity.

## Features

- Encrypt and decrypt configuration files in multiple formats.
- Temporary or persistent key management.
- Modular structure for extensibility.

## Installation

```bash
pip install encryptedconfig
```

## Usage

```python
from encryptedconfig import EncryptedConfigManager

manager = EncryptedConfigManager()
manager.save("config.json", {"key": "value"})
print(manager.load("config.json"))
```