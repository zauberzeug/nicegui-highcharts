# NiceGUI Highcharts

This package is an extension for [NiceGUI](https://github.com/zauberzeug/nicegui), an easy-to-use, Python-based UI framework.
It provides a `highcharts` element based on [Highcharts](https://www.highcharts.com/), the popular JavaScript charting library.
Due to Highcharts' restrictive license, this element is not part of the NiceGUI package anymore, but can be install separately.

## Installation

```bash
python3 -m pip install nicegui_highcharts
```

## Usage

Write your nice GUI in a file `main.py`:

```py
from nicegui import ui
from nicegui_highcharts import highcharts

highcharts({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['A', 'B']},
    'series': [
        {'name': 'Alpha', 'data': [0.1, 0.2]},
        {'name': 'Beta', 'data': [0.3, 0.4]},
    ],
})

ui.run()
```

Launch it with:

```bash
python3 main.py
```
