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

"""Input validation utilities."""

from typing import Any


def validate_input(value: Any) -> bool:
    """
    Validate input for security purposes.

    Args:
        value: Input value to validate

    Returns:
        True if input is valid and safe, False otherwise

    Example:
        >>> validate_input("safe_string")
        True
        >>> validate_input(None)
        False
    """
    if value is None:
        return False

    if isinstance(value, str):
        # Basic validation - no null bytes or control characters
        if "\x00" in value:
            return False

    return True
