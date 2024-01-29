#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

import unittest

import meshcat

import meshcat_shapes


class TestFrame(unittest.TestCase):
    def setUp(self):
        self.visualizer = meshcat.Visualizer().open()

    def test_frame(self):
        meshcat_shapes.frame(self.visualizer["test_frame"])
