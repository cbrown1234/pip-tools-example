

Install pip-tools
```shell
pip install pip-tools
```

Specify real requirements in `requirements.in`

```shell
pip-compile
```

```shell
pip-sync
```

Split out the dev requirements into `requirements-dev.in`

Remember to include `-c requirements.txt` to be fully compatible with
runtime requirements

```
pip-compile
pip-compile requirements-dev.txt
pip-sync requirements-dev.txt requirements.txt
```