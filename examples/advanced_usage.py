#!/usr/bin/env python3
# Copyright 2025 joeathan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Advanced usage example for LegalInkPack.

This example demonstrates advanced features including configuration,
error handling, and input validation.
"""

import logging

from legalinkpack import CounterSurveillance
from legalinkpack.config import Settings
from legalinkpack.utils import validate_input

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def create_configuration():
    """Create and configure settings."""
    logger.info("Creating configuration...")
    settings = Settings()
    settings.set("verbose", True)
    settings.set("debug", False)
    settings.set("custom_option", "value")

    config = settings.to_dict()
    logger.info(f"Configuration created: {config}")
    return config


def safe_scan(cs, target=None):
    """Perform a safe scan with error handling."""
    try:
        logger.info(f"Validating target: {target}")
        if target and not validate_input(target):
            logger.error("Invalid target input")
            return None

        logger.info("Performing scan...")
        result = cs.scan(target=target)
        logger.info(f"Scan completed: {result}")
        return result

    except PermissionError as e:
        logger.error(f"Authorization error: {e}")
        return None
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None


def main():
    """Run advanced usage example."""
    print("LegalInkPack - Advanced Usage Example")
    print("=" * 50)

    # Create configuration
    print("\n1. Setting up configuration...")
    config = create_configuration()

    # Initialize with configuration
    print("\n2. Initializing toolkit with configuration...")
    cs = CounterSurveillance(config=config, verbose=True)
    print("   ✓ Toolkit initialized")

    # Demonstrate input validation
    print("\n3. Testing input validation...")
    test_inputs = [
        "valid_input",
        None,
        "string\x00with_null",
        12345,
    ]

    for test_input in test_inputs:
        is_valid = validate_input(test_input)
        print(f"   Input: {repr(test_input):<25} Valid: {is_valid}")

    # Perform safe scan
    print("\n4. Performing safe scan...")
    result = safe_scan(cs)
    if result:
        print(f"   ✓ Scan successful: {result['status']}")
    else:
        print("   ✗ Scan failed")

    # Demonstrate error handling
    print("\n5. Testing error handling...")
    try:
        invalid_cs = CounterSurveillance(config="invalid_config")
    except ValueError as e:
        print(f"   ✓ Caught expected error: {e}")

    print("\n" + "=" * 50)
    print("Advanced example completed successfully!")


if __name__ == "__main__":
    main()
