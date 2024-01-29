#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

import meshcat
import numpy as np

import meshcat_shapes

if __name__ == "__main__":
    vis = meshcat.Visualizer().open()

    meshcat_shapes.textarea(
        vis["foo"],
        "super easy",
    )

    meshcat_shapes.textarea(
        vis["bar"],
        "barely an inconvenience",
        width=1.5,
        height=1.5,
        font_size=200,
    )

    Rx = meshcat.transformations.rotation_matrix(0.5 * np.pi, [1.0, 0.0, 0.0])
    Rz = meshcat.transformations.rotation_matrix(0.5 * np.pi, [0.0, 0.0, 1.0])
    vis["foo"].set_transform(Rz.dot(Rx))

    trans = meshcat.transformations.translation_matrix([0.0, 1.0, 0.2])
    vis["bar"].set_transform(trans @ Rz @ Rx)

    input("Press Enter to exit...")
