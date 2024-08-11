# Notes

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
- https://datasciencenotebook.org/

## References

### Binder

- [Add a direct Binder link for built HTML notebooks](https://ericmjl.github.io/blog/2020/9/12/add-a-direct-binder-link-for-built-html-notebooks/) blog post by Eric J. Ma

### Deepnote

- [Launch repositories in Deepnote](https://docs.deepnote.com/collaboration/launch-repositories-in-deepnote) documentation

### Google Colab

- https://openincolab.com/:
  - URL: https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/model_monitoring/model_monitoring.ipynb
  - Badge image: https://colab.research.google.com/assets/colab-badge.svg
  - Badge label: Open In Colab
- https://github.com/googlecolab/colabtools/blob/f1f52974c7166bed072014e85b62d19d5e848aec/notebooks/colab-github-demo.ipynb:
  - URL: https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb
  - Badge image: https://colab.research.google.com/assets/colab-badge.svg
  - Badge label: Open In Colab
- [Making Jupyter notebooks Google Colab ready](https://timsainburg.com/google%20colab.html) blog post by Tim Sainburg.
  - https://colab.research.google.com/github/MYUSERNAME/MYREPOSITORY/blob/MYBRANCH/PATH/TO/MYNOTEBOOK.ipynb
- https://github.com/WongKinYiu/yolov9/blob/5b1ea9a8b3f0ffe4fe0e203ec6232d788bb3fcff/README.md
- https://github.com/roboflow/notebooks/blob/dfd4e108a56b7d0fb116577d4cac02155a185422/README.md

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/timsainb/tensorflow2-generative-models/blob/master/1.0-Variational-Autoencoder-fashion-mnist.ipynb)
```

```markdown
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov9-object-detection-on-custom-dataset.ipynb)
```

```markdown
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/grounded-sam-2-auto-label.ipynb)
```
