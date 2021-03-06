# -*- coding: utf-8 -*-

# Copyright 2017 IBM RESEARCH. All Rights Reserved.
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
# =============================================================================

"""
OPENQASM circuit object.

Author: Jim Challenger
"""
from ._qasmexception import QasmException
from ._qasmparser import QasmParser


class Qasm(object):
    """OPENQASM circuit object."""

    def __init__(self, filename=None, data=None):
        """Create an OPENQASM circuit object."""
        if filename is None and data is None:
            raise QasmException("Missing input file and/or data")
        if filename is not None and data is not None:
            raise QasmException("File and data must not both be"
                                + " specified initializing qasm")
        self._filename = filename
        self._data = data

    def print_tokens(self):
        """Parse and print tokens."""
        if self._filename:
            self._data = open(self._filename).read()

        qasm_p = QasmParser(self._filename)
        return qasm_p.print_tokens()

    def parse(self):
        """Parse the data."""
        if self._filename:
            self._data = open(self._filename).read()
        qasm_p = QasmParser(self._filename)
        qasm_p.parse_debug(False)
        return qasm_p.parse(self._data)
