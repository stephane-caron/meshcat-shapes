#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

import math
import time

import meshcat

import meshcat_shapes

if __name__ == "__main__":
    vis = meshcat.Visualizer().open()
    vis["/Background"].set_property("top_color", [200, 220, 250])
    vis["/Background"].set_property("bottom_color", [255] * 3)

    meshcat_shapes.frame(vis["left_frame"])
    meshcat_shapes.frame(vis["right_frame"])
    meshcat_shapes.frame(
        vis["central_frame"],
        axis_length=0.2,
        axis_thickness=0.01,
        opacity=0.8,
        origin_radius=0.02,
    )

    for i in range(800):
        theta = (i + 1) / 100 * 2 * math.pi
        rotation = meshcat.transformations.rotation_matrix(theta, [0, 0, 1])
        y = {"left": -1, "central": 0.0, "right": 1}
        for side in ["left", "central", "right"]:
            trans = meshcat.transformations.translation_matrix([0, y[side], 0])
            vis[f"{side}_frame"].set_transform(trans.dot(rotation))
        time.sleep(0.01)
