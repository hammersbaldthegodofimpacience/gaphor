# Gaphor on macOS

The latest release of Gaphor can be downloaded from the [Gaphor download page](https://gaphor.org/download#macos). Gaphor can also be installed as a [Homebrew cask](https://formulae.brew.sh/cask/gaphor).

Older releases are available from [GitHub](https://github.com/gaphor/gaphor/releases).

[CI builds](https://github.com/gaphor/gaphor/actions/workflows/full-build.yml) are also available.


## Development Environment

To setup a development environment with macOS:
1. Install [Homebrew](https://brew.sh)
1. Open a terminal and execute:
```bash
brew install python3 gobject-introspection gtk4 gtksourceview5 libadwaita adwaita-icon-theme graphviz
```
Install [Poetry](https://python-poetry.org) using [pipx](https://pypa.github.io/pipx/):
```bash
pipx install poetry
```

[Clone the
repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
```bash
cd gaphor
poetry config virtualenvs.in-project true
poetry install
poetry run gaphor
```

If PyGObject does not compile and complains about a missing `ffi.h` file, set the following
environment variable and run `poetry install` again:
```bash
export PKG_CONFIG_PATH=/usr/local/opt/libffi/lib/pkgconfig
poetry install
```

### Debugging using Visual Studio Code

Before you start debugging you'll need to open Gaphor is VSCode (the folder
containing `pyproject.toml`). You'll need to have the Python extension installed.

Create a file `.vscode/launch.json` with the following content:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Gaphor UI",
            "type": "python",
            "request": "launch",
            "module": "gaphor",
            "justMyCode": false,
        }
    ]
}
```

## Packaging for macOS

In order to create an exe installation package for macOS, we utilize
[PyInstaller](https://pyinstaller.org) which analyzes Gaphor to find all the
dependencies and bundle them in to a single folder.

1. Follow the instructions for settings up a development environment above
1. Open a terminal and execute the following from the repository directory:
```bash
poetry install --with packaging
poetry run poe package
```
