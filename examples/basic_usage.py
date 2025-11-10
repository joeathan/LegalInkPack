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
Basic usage example for LegalInkPack.

This example demonstrates the basic functionality of the CounterSurveillance toolkit.
"""

from legalinkpack import CounterSurveillance


def main():
    """Run basic usage example."""
    print("LegalInkPack - Basic Usage Example")
    print("=" * 50)

    # Initialize the toolkit
    print("\n1. Initializing CounterSurveillance toolkit...")
    cs = CounterSurveillance(verbose=True)
    print("   ✓ Toolkit initialized")

    # Check status
    print("\n2. Checking toolkit status...")
    status = cs.get_status()
    print(f"   Status: {status['status']}")
    print(f"   Version: {status['version']}")
    print(f"   Config loaded: {status['config_loaded']}")

    # List capabilities
    print("\n3. Listing capabilities...")
    capabilities = cs.list_capabilities()
    for cap in capabilities:
        print(f"   - {cap}")

    # Perform a scan
    print("\n4. Performing scan...")
    result = cs.scan()
    print(f"   Scan status: {result['status']}")
    print(f"   Message: {result['message']}")

    print("\n" + "=" * 50)
    print("Example completed successfully!")


if __name__ == "__main__":
    main()
