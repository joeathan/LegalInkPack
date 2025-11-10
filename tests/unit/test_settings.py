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

"""Tests for configuration settings."""

from legalinkpack.config.settings import Settings


class TestSettings:
    """Test cases for Settings class."""

    def test_initialization(self) -> None:
        """Test Settings initialization."""
        settings = Settings()
        assert settings is not None

    def test_default_values(self) -> None:
        """Test that default values are set."""
        settings = Settings()
        assert settings.get("version") == "0.1.0"
        assert settings.get("debug") is False
        assert settings.get("log_level") == "INFO"

    def test_get_existing_key(self) -> None:
        """Test getting an existing configuration value."""
        settings = Settings()
        value = settings.get("version")
        assert value == "0.1.0"

    def test_get_missing_key(self) -> None:
        """Test getting a missing key returns None."""
        settings = Settings()
        value = settings.get("nonexistent")
        assert value is None

    def test_get_with_default(self) -> None:
        """Test getting a missing key with default value."""
        settings = Settings()
        value = settings.get("nonexistent", "default_value")
        assert value == "default_value"

    def test_set_value(self) -> None:
        """Test setting a configuration value."""
        settings = Settings()
        settings.set("new_key", "new_value")
        assert settings.get("new_key") == "new_value"

    def test_to_dict(self) -> None:
        """Test converting settings to dictionary."""
        settings = Settings()
        config_dict = settings.to_dict()
        assert isinstance(config_dict, dict)
        assert "version" in config_dict
        assert config_dict["version"] == "0.1.0"
