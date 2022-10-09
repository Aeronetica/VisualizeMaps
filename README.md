# VisualizeMaps - Map visualization tool based on the QGIS python development enviornment.

![Coveralls GitHub](https://img.shields.io/coveralls/github/io-aero/VisualizeMaps.svg)
![GitHub (Pre-)Release](https://img.shields.io/github/v/release/io-aero/VisualizeMaps?include_prereleases)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/KonnexionsGmbh/VisualizeMaps)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/io-aero/VisualizeMaps/0.9.8)

## 1. What is VisualizeMaps?
VisualizeMaps is a graphical visualization tool used to verify GIS maps of different kinds.  It allows visualization of both raster and vector maps, which it displays on a background of shaded relief terrain, Bing satalite maps, and Bing placename maps.  The tool allows cycling through different maps in order to see how different maps change, or it allows for the simultanous display of all the maps.  Vector maps are displayed on top of the raster maps and satalitte background, by default.

VisualizeMaps will contain the following features
- Raster loading and display
- Vector loading and display
- Query tool which gives the lat, lon (or north east UTM), and value of all rasters at a particular location that you select
- **TODO** Add features as they are needed

## 2. Directory and File Structure of this Repository

### 2.1 Directories

| Directory         | Content                                                 |
|-------------------|---------------------------------------------------------|
| .github/workflows | [GitHub Action](https://github.com/actions) workflows.  |
| docs              | **`VisualizeMaps`** documentation files.                |
| resources         | Selected manuals etc.                                   |
| scripts           | Ubuntu and Windows scripts for running the application. |
| src               | Python scripts.                                         |
| tests             | Scripts and data for pytest.                            |

### 2.2 Files

| File                | Functionality                                                                                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .gitignore          | Configuration of files and folders to be ignored.                                                                                                                       |
| LICENSE             | Text of the licence terms.                                                                                                                                              |
| logging_cfg.yaml    | Configuration of the Logger functionality.                                                                                                                              |
| Makefile            | Definition of tasks to be executed with the `make` command.                                                                                                             |
| Pipfile             | Definition of the Python package requirements.                                                                                                                          |
| Pipfile.lock        | Definition of the specific versions of the Python packages.                                                                                                             |
| pyproject.toml      | Configuration file for [isort](https://github.com/PyCQA/isort), [pydocstyle](https://github.com/PyCQA/pydocstyle), and [pytest](https://github.com/pytest-dev/pytest/). |
| README.md           | This file.                                                                                                                                                              |
| setup.cfg           | Configuration file for [flake8](https://github.com/pycqa/flake8), and **VisualizeMaps**.                                                                               |
