# Usage Guide

This guide covers basic to advanced usage of LegalInkPack.

## Quick Start

```python
from legalinkpack import CounterSurveillance

# Initialize the toolkit
cs = CounterSurveillance()

# Perform a basic scan
result = cs.scan()
print(result)
```

## Basic Usage

### Initialization

```python
from legalinkpack import CounterSurveillance

# Basic initialization
cs = CounterSurveillance()

# With configuration
config = {
    "verbose": True,
    "timeout": 30
}
cs = CounterSurveillance(config=config)

# With verbose mode
cs = CounterSurveillance(verbose=True)
```

### Running Scans

```python
# Basic scan
result = cs.scan()

# Scan with target (requires authorization)
result = cs.scan(target="authorized_target")
```

### Checking Status

```python
# Get toolkit status
status = cs.get_status()
print(status)

# List available capabilities
capabilities = cs.list_capabilities()
print(capabilities)
```

## Configuration

### Configuration Options

```python
config = {
    "verbose": True,       # Enable verbose logging
    "timeout": 30,         # Operation timeout in seconds
    "log_level": "INFO",   # Logging level
}

cs = CounterSurveillance(config=config)
```

### Using Settings Manager

```python
from legalinkpack.config import Settings

settings = Settings()
settings.set("debug", True)
settings.set("custom_option", "value")

# Get configuration as dictionary
config = settings.to_dict()
```

## Advanced Usage

### Input Validation

```python
from legalinkpack.utils import validate_input

# Validate user input
user_input = "some_input"
if validate_input(user_input):
    # Process input
    result = cs.scan(target=user_input)
else:
    print("Invalid input")
```

### Error Handling

```python
from legalinkpack import CounterSurveillance

try:
    cs = CounterSurveillance(config={"key": "value"})
    result = cs.scan(target="unauthorized")
except ValueError as e:
    print(f"Configuration error: {e}")
except PermissionError as e:
    print(f"Authorization error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Legal and Ethical Considerations

### Authorization Requirements

**Always ensure you have proper authorization before scanning:**

```python
# Good practice - check authorization first
def safe_scan(target):
    if has_authorization(target):
        cs = CounterSurveillance()
        return cs.scan(target=target)
    else:
        raise PermissionError("No authorization for target")
```

### Logging and Auditing

**Maintain audit trails:**

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cs = CounterSurveillance(verbose=True)
logger.info("Starting authorized scan")
result = cs.scan()
logger.info(f"Scan completed: {result}")
```

## Best Practices

1. **Always use virtual environments**
2. **Keep the toolkit updated**
3. **Validate all inputs**
4. **Handle errors gracefully**
5. **Maintain audit logs**
6. **Follow legal requirements**
7. **Use configuration files for sensitive settings**
8. **Never hardcode credentials**

## Examples

See the [examples directory](../examples/) for complete working examples:

- Basic usage
- Configuration management
- Error handling
- Advanced features

## Command Line Interface

(To be implemented in future versions)

```bash
# Check version
legalinkpack --version

# Run scan
legalinkpack scan --target authorized_target

# Get help
legalinkpack --help
```

## Integration

### With Other Tools

```python
# Integration example
from legalinkpack import CounterSurveillance
import other_security_tool

cs = CounterSurveillance()
result = cs.scan()

# Use result with other tools
other_security_tool.analyze(result)
```

## Troubleshooting

### Common Issues

**Issue: Permission denied during scan**
- Ensure you have proper authorization
- Check target configuration
- Review security policies

**Issue: Configuration not loading**
- Verify configuration format
- Check for syntax errors
- Ensure required fields are present

## Next Steps

- Review [API Reference](api.md)
- Check [Examples](../examples/)
- Read [Security Policy](../SECURITY.md)
- Contribute via [Contributing Guide](../CONTRIBUTING.md)
