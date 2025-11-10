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

"""Tests for core countersurveillance functionality."""

import pytest

from legalinkpack.core.countersurveillance import CounterSurveillance


class TestCounterSurveillance:
    """Test cases for CounterSurveillance class."""

    def test_initialization(self) -> None:
        """Test CounterSurveillance initialization."""
        cs = CounterSurveillance()
        assert cs is not None
        assert cs.config == {}
        assert cs.verbose is False

    def test_initialization_with_config(self) -> None:
        """Test CounterSurveillance initialization with config."""
        config = {"key": "value"}
        cs = CounterSurveillance(config=config)
        assert cs.config == config

    def test_initialization_with_verbose(self) -> None:
        """Test CounterSurveillance initialization with verbose flag."""
        cs = CounterSurveillance(verbose=True)
        assert cs.verbose is True

    def test_invalid_config(self) -> None:
        """Test that invalid config raises ValueError."""
        with pytest.raises(ValueError):
            CounterSurveillance(config="invalid")  # type: ignore

    def test_scan_basic(self) -> None:
        """Test basic scan functionality."""
        cs = CounterSurveillance()
        result = cs.scan()
        assert "status" in result
        assert result["status"] == "ready"
        assert "message" in result
        assert "version" in result

    def test_get_status(self) -> None:
        """Test get_status method."""
        cs = CounterSurveillance()
        status = cs.get_status()
        assert "status" in status
        assert status["status"] == "active"
        assert "version" in status
        assert "config_loaded" in status

    def test_list_capabilities(self) -> None:
        """Test list_capabilities method."""
        cs = CounterSurveillance()
        capabilities = cs.list_capabilities()
        assert isinstance(capabilities, list)
        assert len(capabilities) > 0
        assert "scan" in capabilities
        assert "status" in capabilities
