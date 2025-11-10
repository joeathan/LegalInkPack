# API Reference

Complete API documentation for LegalInkPack.

## Core Module

### CounterSurveillance

Main class for countersurveillance operations.

```python
from legalinkpack import CounterSurveillance
```

#### `__init__(config=None, verbose=False)`

Initialize the CounterSurveillance toolkit.

**Parameters:**
- `config` (dict, optional): Configuration dictionary
- `verbose` (bool, optional): Enable verbose output. Default: False

**Raises:**
- `ValueError`: If configuration is invalid

**Example:**
```python
cs = CounterSurveillance(config={"key": "value"}, verbose=True)
```

#### `scan(target=None)`

Perform a security scan.

**Parameters:**
- `target` (str, optional): Target identifier for scanning

**Returns:**
- `dict`: Scan results with status, message, and version

**Raises:**
- `ValueError`: If target specification is invalid
- `PermissionError`: If operation is not authorized

**Example:**
```python
result = cs.scan()
print(result['status'])
```

#### `get_status()`

Get current toolkit status.

**Returns:**
- `dict`: Status information including:
  - `status` (str): Current status
  - `version` (str): Toolkit version
  - `config_loaded` (bool): Whether configuration is loaded

**Example:**
```python
status = cs.get_status()
print(status)
```

#### `list_capabilities()`

List available capabilities.

**Returns:**
- `list[str]`: List of capability names

**Example:**
```python
capabilities = cs.list_capabilities()
for cap in capabilities:
    print(cap)
```

## Utilities Module

### validation

Input validation utilities.

```python
from legalinkpack.utils import validate_input
```

#### `validate_input(value)`

Validate input for security purposes.

**Parameters:**
- `value` (Any): Input value to validate

**Returns:**
- `bool`: True if valid and safe, False otherwise

**Example:**
```python
if validate_input(user_input):
    process(user_input)
```

## Configuration Module

### Settings

Configuration settings manager.

```python
from legalinkpack.config import Settings
```

#### `__init__()`

Initialize settings with default values.

**Example:**
```python
settings = Settings()
```

#### `get(key, default=None)`

Get configuration value.

**Parameters:**
- `key` (str): Configuration key
- `default` (Any, optional): Default value if key not found

**Returns:**
- `Any`: Configuration value or default

**Example:**
```python
value = settings.get("debug", False)
```

#### `set(key, value)`

Set configuration value.

**Parameters:**
- `key` (str): Configuration key
- `value` (Any): Configuration value

**Example:**
```python
settings.set("debug", True)
```

#### `to_dict()`

Get all configuration as dictionary.

**Returns:**
- `dict`: Copy of configuration dictionary

**Example:**
```python
config = settings.to_dict()
```

## Module Constants

### Version Information

```python
import legalinkpack

print(legalinkpack.__version__)  # "0.1.0"
print(legalinkpack.__author__)   # "joeathan"
print(legalinkpack.__license__)  # "Apache-2.0"
```

## Type Hints

LegalInkPack uses type hints throughout. Example:

```python
from typing import Dict, Optional
from legalinkpack import CounterSurveillance

def scan_target(target: Optional[str] = None) -> Dict[str, str]:
    cs = CounterSurveillance()
    return cs.scan(target)
```

## Exceptions

### ValueError

Raised when configuration or input is invalid.

```python
try:
    cs = CounterSurveillance(config="invalid")
except ValueError as e:
    print(f"Invalid configuration: {e}")
```

### PermissionError

Raised when operation is not authorized.

```python
try:
    result = cs.scan(target="unauthorized")
except PermissionError as e:
    print(f"Not authorized: {e}")
```

## Best Practices

### Type Safety

Use type hints and mypy for type checking:

```python
from typing import Dict
from legalinkpack import CounterSurveillance

def create_scanner(config: Dict[str, str]) -> CounterSurveillance:
    return CounterSurveillance(config=config)
```

### Error Handling

Always handle potential exceptions:

```python
try:
    cs = CounterSurveillance()
    result = cs.scan()
except (ValueError, PermissionError) as e:
    logging.error(f"Operation failed: {e}")
    raise
```

## Examples

### Complete Example

```python
from legalinkpack import CounterSurveillance
from legalinkpack.config import Settings
from legalinkpack.utils import validate_input

# Setup configuration
settings = Settings()
settings.set("verbose", True)
config = settings.to_dict()

# Initialize toolkit
cs = CounterSurveillance(config=config)

# Validate and scan
target = "example_target"
if validate_input(target):
    try:
        result = cs.scan(target=target)
        print(f"Scan result: {result}")
    except PermissionError as e:
        print(f"Authorization failed: {e}")
else:
    print("Invalid target")
```

## See Also

- [Usage Guide](usage.md)
- [Installation Guide](installation.md)
- [Examples](../examples/)
