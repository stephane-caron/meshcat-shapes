# meshcat-shapes

[![Build](https://img.shields.io/github/actions/workflow/status/stephane-caron/meshcat-shapes/build.yml?branch=main)](https://github.com/stephane-caron/meshcat-shapes/actions)
[![Documentation](https://img.shields.io/github/actions/workflow/status/stephane-caron/meshcat-shapes/docs.yml?branch=main&label=docs)](https://stephane-caron.github.io/meshcat-shapes/)
[![Coverage](https://coveralls.io/repos/github/stephane-caron/meshcat-shapes/badge.svg?branch=main)](https://coveralls.io/github/stephane-caron/meshcat-shapes?branch=main)
[![PyPI version](https://img.shields.io/pypi/v/meshcat-shapes)](https://pypi.org/project/meshcat-shapes/)

Useful shapes to decorate MeshCat scenes.

## Installation

```console
pip install meshcat-shapes
```

## Shapes

| [``meshcat_shapes.frame``](https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.frame) | ``meshcat_shapes.point`` | ``meshcat_shapes.textarea`` |
|--------------------------|--------------------------|-----------------------------|
| <a href="https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.frame"><img src="https://github.com/stephane-caron/meshcat-shapes/raw/main/gallery/frame.png" width="250"></a> | <img src="https://github.com/stephane-caron/meshcat-shapes/raw/main/gallery/point.png" width="250"> | <img src="https://github.com/stephane-caron/meshcat-shapes/raw/main/gallery/textarea.png" width="250"> |

PRs are welcome: open one if you have implemented a shape that can be useful to others.

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

meshcat_shapes.point(
    vis["red_point"],
    opacity=0.3,
    radius=0.05,
    color=0xFF0000,
)

meshcat_shapes.textarea(vis["text"], "super easy")
```
