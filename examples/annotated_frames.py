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

    meshcat_shapes.frame(vis["left"])

    meshcat_shapes.frame(
        vis["right"],
        axis_length=0.2,
        axis_thickness=0.01,
        opacity=0.8,
        origin_radius=0.02,
    )

    vis["left"].set_transform(
        meshcat.transformations.translation_matrix([0.0, -1.0, 0.2])
    )
    vis["right"].set_transform(
        meshcat.transformations.translation_matrix([0.0, 1.0, -0.2])
    )

    for frame in ("left", "right"):
        meshcat_shapes.textarea(
            vis[frame]["text"],
            f"{frame} frame",
            width=0.5,
            height=0.5,
        )

        Rx = meshcat.transformations.rotation_matrix(
            0.5 * np.pi, [1.0, 0.0, 0.0]
        )
        Rz = meshcat.transformations.rotation_matrix(
            0.5 * np.pi, [0.0, 0.0, 1.0]
        )
        trans = meshcat.transformations.translation_matrix([0.0, 0.0, 0.03])
        vis[frame]["text"].set_transform(trans @ Rz @ Rx)
