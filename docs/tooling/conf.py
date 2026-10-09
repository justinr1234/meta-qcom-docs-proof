"""Sphinx configuration for the meta-qcom reference proof site."""

from pathlib import Path

project = "meta-qcom Reference Documentation"
copyright = "Qualcomm Technologies, Inc. and/or its subsidiaries"
author = "meta-qcom maintainers"

extensions = ["myst_parser"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "README.md"]
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
master_doc = "index"
html_theme = "alabaster"
html_title = "meta-qcom Reference Documentation"
html_copy_source = False

root = Path(__file__).parent
html_extra_path = [str(root / "route-manifest.txt")]
