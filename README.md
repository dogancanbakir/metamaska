#  μετάμάσκα - malevolent payload classifier
meta.mask can detect different types of malicious payloads like SQL injection, XSS, path-traversal, and command injection payloads.

[![pypi](https://img.shields.io/pypi/v/metamaska.svg)](https://pypi.org/project/metamaska/)
[![python](https://img.shields.io/pypi/pyversions/metamaska.svg)](https://pypi.org/project/metamaska/)
[![Build Status](https://github.com/dogancanbakir/metamaska/actions/workflows/dev.yml/badge.svg)](https://github.com/dogancanbakir/metamaska/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/dogancanbakir/metamaska/branch/main/graphs/badge.svg)](https://codecov.io/github/dogancanbakir/metamaska)


* Documentation: <https://dogancanbakir.github.io/metamaska>
* GitHub: <https://github.com/dogancanbakir/metamaska>
* PyPI: <https://pypi.org/project/metamaska/>
* Free software: MIT


## Basic Use
# CLI: 
```shell
$ python run.py
Usage: run.py [OPTIONS]

Options:
  -m, --meta TEXT      meta string to evaluate  [required]
  -p, --proba BOOLEAN  probability of given meta
  --help               Show this message and exit.
 ```
 Example:
 ```shell
 python3 run.py -m "<script>alert(1)</script>" -p true
 ```

 # API
 The example API runs on port 8001. It reads in a base64 encoded string in the JSON `meta` field and returns a JSON response with the attack type and probability. 

 Note: This should *not* be used for production.
 ```shell
 curl -X POST -H "Content-Type: application/json" -d '{"meta": "PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pgo="}' http://localhost:8001/classify
 ```
The API also includes the endpoint `/environment` to report the app's modules and versions.

## TODO

* support more types
* support interoperable model formats, more at [here](https://scikit-learn.org/stable/model_persistence.html#interoperable-formats)

## Credits

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage)
- [ML-based-WAF](https://github.com/vladan-stojnic/ML-based-WAF)
- [WAF-A-MoLE](https://github.com/AvalZ/WAF-A-MoLE)
