# python-simple-ci
This project explores how to build a Python package using  industry-standard project organization and how to connect the project to Github CI for linting and unit testing in both conda and pip virtual environments.


## sharing the environment for this package
### conda file readable by Windows, macOS, Linux
Import this version when user has the same platform (Anaconda, Miniconda) as the author.
```shell script
$ conda env export --name ENVNAME > envname.yml

$ conda env create --file envname.yml
```

### conda file with exact package versions for one OS
```shell script
$ conda list --explicit > pkgs.txt

$ conda create --name NEWENV --file pkgs.txt
```

### conda file with only the packages added by the user
Import this version when other export options result in "ResolvePackageNotFound" when setting up a virtual environment.
```shell script
$ conda env export --from-history -f platformless.yml

$ conda env create --file platformless.yml
```

### pip file
Import this version when using pip or when using conda and the conda yaml file is missing.
```shell script
$ pip freeze > requirements.txt

$ pip install -r requirements.txt   # install via pip

$ while read req; do conda install --yes $req; done < requirements.txt  # install via conda
```

## distributing this package
### Anaconda Cloud
(tbd)
### PyPI
(tbd)
