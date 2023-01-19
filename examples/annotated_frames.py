#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
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

import meshcat
import meshcat_shapes
import numpy as np

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
