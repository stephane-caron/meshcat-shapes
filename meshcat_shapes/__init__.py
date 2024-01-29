#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

"""Useful shapes to decorate MeshCat scenes."""

__version__ = "0.3.0"

from .frame import frame
from .point import point
from .textarea import textarea

__all__ = [
    "frame",
    "point",
    "textarea",
]
