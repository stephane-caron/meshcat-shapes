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
