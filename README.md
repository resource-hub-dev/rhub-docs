# RHub documentation

All documentation, style guides, contributing guides, etc. in one place.

https://rhub.readthedocs.io/

## Build

```sh
# install dependencies
pip3 install -U -r requirements.txt
# build HTML
make clean html
```

## View

To view HTML output you need to start HTTP server, opening local files
(`file://`) in browser may not work.

```sh
# start HTTP server on port 9000 serving content from _build/html directory
python3 -m http.server -d _build/html 9000
```
