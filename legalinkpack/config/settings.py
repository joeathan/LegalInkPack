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

"""Configuration settings management."""

from typing import Any, Dict


class Settings:
    """
    Configuration settings manager.

    This class handles loading, validating, and managing configuration
    settings for the toolkit.

    Attributes:
        _config: Internal configuration dictionary
    """

    def __init__(self) -> None:
        """Initialize settings with default values."""
        self._config: Dict[str, Any] = {
            "version": "0.1.0",
            "debug": False,
            "log_level": "INFO",
        }

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.

        Args:
            key: Configuration key
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value.

        Args:
            key: Configuration key
            value: Configuration value
        """
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """
        Get all configuration as dictionary.

        Returns:
            Copy of configuration dictionary
        """
        return self._config.copy()
