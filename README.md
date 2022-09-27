# meshcat-shapes

[![Build](https://img.shields.io/github/workflow/status/stephane-caron/robot_descriptions.py/CI)](https://github.com/stephane-caron/robot_descriptions.py/actions)
[![Coverage](https://coveralls.io/repos/github/stephane-caron/robot_descriptions.py/badge.svg?branch=master)](https://coveralls.io/github/stephane-caron/robot_descriptions.py?branch=master)
[![PyPI version](https://img.shields.io/pypi/v/robot_descriptions)](https://pypi.org/project/robot_descriptions/)
[![Contributing](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/stephane-caron/robot_descriptions.py/tree/master/CONTRIBUTING.md)

Useful shapes to decorate MeshCat scenes.

## Installation

```console
pip install meshcat-shapes
```

## Shapes

| ``meshcat_shapes.frame`` |
|--------------------------|
| <img src="https://github.com/stephane-caron/meshcat-shapes/raw/main/gallery/frame.png" width="250"> |

## Usage

```python
import meshcat
import meshcat_shapes

vis = meshcat.Visualizer().open()

meshcat_shapes.frame(
    vis["my_frame"],
    axis_length=0.2,
    axis_thickness=0.01,
    opacity=0.8,
    origin_radius=0.02,
)
```
