# nbadge

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

Generate badges from Jupyter notebooks hosted on GitHub for different services.

## Usage

### Via [pipx](https://github.com/pypa/pipx)

```bash
pipx run nbadge --help
```

```bash
pipx run nbadge
```

## Development

- `pdm config python.use_venv False` + `pdm config python.use_venv`
- `pdm install`
- `pdm run nbadge --help`
- `pdm run nbadge https://github.com/feedzai/feedzai-altair-theme/blob/master/demo.ipynb`
- `pdm run black .` + `pdm run isort .`
