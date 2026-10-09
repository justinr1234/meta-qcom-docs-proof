---
page_type: reference
---

# Layer Metadata

The layer metadata in `conf/layer.conf`:

| Setting | Value |
| --- | --- |
| Collection | `qcom` |
| Priority | `6` |
| Required dependency | `core` |
| Recommended layers | `openembedded-layer meta-arm` |
| Compatible series | `blacksail` |
| Baseline variable | `main` |

The same file adds `recipes-*` BitBake files to `BBFILES`, registers optional
dynamic layers, exposes the layer root as `LAYERDIR_qcom`, and enables the
`qli-mirrors` class through `INHERIT`.
