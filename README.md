# The Hitchhiker's Guide to AI

An easy-to-understand e-book covering AI fundamentals, large language models, and AI agent development.

**Language:** English | [한국어](README.ko.md)

📖 **Read online:** [ai.qu3vipon.com](https://ai.qu3vipon.com)

## Local preview

Requires Python 3.12 or newer.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/site.py serve
```

Build both editions with `python scripts/site.py build`. English is served at `/`, Korean at `/ko/`. The preview builds once; restart it after editing. See [language structure and translation workflow](docs-i18n.md).

## License

This project is licensed under [CC BY-NC-ND 4.0](LICENSE). Non-commercial sharing with attribution is allowed; commercial use and distribution of modified versions are not permitted.
