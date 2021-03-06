# nbadge

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

A Python CLI to generate Jupyter notebook badges for different services.

## References

- [Add a direct Binder link for built HTML notebooks](https://ericmjl.github.io/blog/2020/9/12/add-a-direct-binder-link-for-built-html-notebooks/) blog post by Eric J. Ma.
- [Launch repositories in Deepnote](https://docs.deepnote.com/collaboration/launch-repositories-in-deepnote) documentation.
- [Making Jupyter notebooks Google Colab ready](https://timsainburg.com/google%20colab.html) blog post by Tim Sainburg.
- [Open in Colab](https://openincolab.com/) website.

## Development

- `pdm config python.use_venv False` + `pdm config python.use_venv`
- `pdm install`
- `pdm run nbadge --help`
- `pdm run nbadge https://github.com/feedzai/feedzai-altair-theme/blob/master/demo.ipynb`
- `pdm run black .` + `pdm run isort .`

## Notes

- [PEP 582](https://peps.python.org/pep-0582/): Python local packages directory.
- `eval "$(pdm --pep582)"` ([source](https://pdm.fming.dev/#for-mac-and-linux-users)).
- [Awesome PDM](https://github.com/pdm-project/awesome-pdm).
- [PDM](https://pdm.fming.dev/latest/) documentation. [Publish the project to PyPI](https://pdm.fming.dev/latest/usage/project/#publish-the-project-to-pypi). [License](https://peps.python.org/pep-0621/#license).
- Commands:
  - `pdm --version`.
  - `pdm init`.
  - `pdm config python.use_venv False` and `pdm install`.
  - `pdm config python.use_venv True` and `pdm install`.
  - `pdm add click pyperclip`.
  - `pdm add -dG format black isort`.
  - `pdm build --no-isolation --verbose`.
- [Setup PDM for GitHub Action](https://github.com/marketplace/actions/setup-pdm).
- [Copier template](https://github.com/pdm-project/copier-pdm) and [Copier template by pawamoy](https://github.com/pawamoy/copier-pdm).
- [giturlparse](https://github.com/nephila/giturlparse) package.
- `curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 - -v 2.0.2`.
