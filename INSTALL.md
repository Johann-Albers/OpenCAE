# Building OpenCAE from Source

Below are instructions for building OpenCAE
- on some popular Linux distributions

## Getting OpenCAE source

You can get the sources to the latest development version from our git
repository:

```
git clone http://github.com/albers3/opencae.git
cd opencae
```

You keep it updated by using:

```
git checkout main
git pull -r
```

## Build options for OpenCAE

### Building the development version of OpenCAE under Linux

You can build the shared library from within the [core](/core) folder by
using the make command. You can build the complete library by using:

```
make
```

After you have built the library, you can build all tests using:

```
make test
```

And run all of them using:

```
make test_all
```

After you have built the library (tests are optionally), you can build
the python package from within the [python](/python) folder by using:

```
pip install -e .
```

On successful build of the library and the python package, you can run
the python examples in the [examples](/examples) folder. For example, to
run the geometry from step example, go into the [examples](/examples)
folder and run:

```
./geometry_from_step
```
