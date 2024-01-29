#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

import time

import meshcat
import numpy as np

import meshcat_shapes

if __name__ == "__main__":
    vis = meshcat.Visualizer().open()

    meshcat_shapes.point(vis["left_point"])

    meshcat_shapes.point(
        vis["right_point"],
        color=0x00FF00,
        opacity=0.8,
        radius=0.05,
    )

    meshcat_shapes.point(
        vis["central_point"],
        color=0xFF0000,
        radius=0.02,
    )

    side = {"left_point": -1, "central_point": 0.0, "right_point": 1}
    for i in range(900 + 75):
        theta = 2 * np.pi * i / 300
        for name in ["left_point", "central_point", "right_point"]:
            y = side[name] * np.sin(theta)
            trans = meshcat.transformations.translation_matrix([0.0, y, 0.0])
            vis[name].set_transform(trans)
        time.sleep(0.01)
