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

"""Tests for validation utilities."""

from legalinkpack.utils.validation import validate_input


class TestValidation:
    """Test cases for validation utilities."""

    def test_validate_input_none(self) -> None:
        """Test that None input is invalid."""
        assert validate_input(None) is False

    def test_validate_input_string(self) -> None:
        """Test that valid string input is accepted."""
        assert validate_input("safe_string") is True

    def test_validate_input_null_byte(self) -> None:
        """Test that string with null byte is rejected."""
        assert validate_input("string\x00with_null") is False

    def test_validate_input_number(self) -> None:
        """Test that number input is accepted."""
        assert validate_input(42) is True

    def test_validate_input_dict(self) -> None:
        """Test that dict input is accepted."""
        assert validate_input({"key": "value"}) is True

    def test_validate_input_list(self) -> None:
        """Test that list input is accepted."""
        assert validate_input([1, 2, 3]) is True
