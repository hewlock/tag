Test everything
---------------
* [ ] `make test`

Make a release commit
---------------------
* [ ] Update the version number in `tag/__init__.py`
* [ ] `make docs`
* [ ] Write changelog entry
* [ ] Commit `git commit -m "v.X.Y.Z"`
* [ ] Tag `git tag -a vX.Y.Z -m "vX.Y.Z"`
* [ ] Push release and tag

Make a PyPI release
-------------------
* [ ] `make clean`
* [ ] `python setup.py sdist`
* [ ] `twine upload dist/*`
