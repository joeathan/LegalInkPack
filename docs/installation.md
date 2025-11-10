# Installation Guide

This guide provides detailed instructions for installing LegalInkPack.

## Prerequisites

Before installing LegalInkPack, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (recommended)
- Git (for development installation)

### System Requirements

**Minimum:**
- Python 3.8+
- 256 MB RAM
- 50 MB disk space

**Recommended:**
- Python 3.11+
- 512 MB RAM
- 100 MB disk space

## Installation Methods

### Method 1: PyPI (Recommended for Users)

Once published to PyPI:

```bash
pip install legalinkpack
```

### Method 2: From Source (Recommended for Developers)

```bash
# Clone the repository
git clone https://github.com/joeathan/LegalInkPack.git
cd LegalInkPack

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Method 3: Direct from GitHub

```bash
pip install git+https://github.com/joeathan/LegalInkPack.git
```

## Virtual Environment Setup

We strongly recommend using a virtual environment:

```bash
# Create virtual environment
python -m venv legalinkpack-env

# Activate on Linux/macOS
source legalinkpack-env/bin/activate

# Activate on Windows
legalinkpack-env\Scripts\activate

# Install LegalInkPack
pip install legalinkpack
```

## Verifying Installation

After installation, verify it works:

```python
python -c "import legalinkpack; print(legalinkpack.__version__)"
```

Or run the test suite:

```bash
pytest
```

## Development Installation

For contributing to LegalInkPack:

```bash
# Clone and enter directory
git clone https://github.com/joeathan/LegalInkPack.git
cd LegalInkPack

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install with development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run tests to verify
pytest
```

## Troubleshooting

### Common Issues

**Issue: pip install fails**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Try again
pip install legalinkpack
```

**Issue: Permission denied**
```bash
# Use --user flag
pip install --user legalinkpack
```

**Issue: Python version mismatch**
```bash
# Check your Python version
python --version

# Use specific Python version
python3.11 -m pip install legalinkpack
```

### Getting Help

If you encounter issues:

1. Check the [FAQ](faq.md)
2. Search [existing issues](https://github.com/joeathan/LegalInkPack/issues)
3. Open a [new issue](https://github.com/joeathan/LegalInkPack/issues/new)

## Uninstallation

To uninstall LegalInkPack:

```bash
pip uninstall legalinkpack
```

## Next Steps

- Read the [Usage Guide](usage.md)
- Review the [API Reference](api.md)
- Check out [Examples](../examples/)
- Read [Contributing Guide](../CONTRIBUTING.md)
