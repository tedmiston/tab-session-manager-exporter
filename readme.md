# Tab Session Manager Exporter

The [Tab Session Manager](https://github.com/sienori/Tab-Session-Manager) export JSON output file is very complex with tons of properties and deeply nested structure.  It's virtually impossible to read.

To solve this, we parse out only the essential properties and use those to build a much simpler YAML output that is easily human readable.

## Setup

```
pipenv install
```

## Quickstart

Export your sessions from:

```plain
Tab Session Manager >
  Settings >
    Sessions >
      Export Sessions >
        Export
```

and save them as `sessions.json`.

Then run:

```
pipenv run python app.py
```
