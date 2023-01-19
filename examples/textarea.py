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

    meshcat_shapes.textarea(
        vis["foo"],
        "actually it's going to be super easy",
        font_size=10,
        width=1,
        height=1,
    )

    meshcat_shapes.textarea(vis["bar"], "barely an inconvenience", font_size=5)

    Rx = meshcat.transformations.rotation_matrix(0.5 * np.pi, [1.0, 0.0, 0.0])
    Rz = meshcat.transformations.rotation_matrix(0.5 * np.pi, [0.0, 0.0, 1.0])
    vis["foo"].set_transform(Rz.dot(Rx))
    vis["bar"].set_transform(Rz.dot(Rx))
