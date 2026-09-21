#!/usr/bin/env python3
from nicegui import ui

ui.highchart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['A', 'B']},
    'series': [
        {'name': 'Alpha', 'data': [0.1, 0.2]},
        {'name': 'Beta', 'data': [0.3, 0.4]},
    ],
})

ui.highchart({
    'title': False,
    'chart': {'type': 'solidgauge'},
    'yAxis': {'min': 0, 'max': 1},
    'series': [
        {'data': [0.42]},
    ],
}, extras=['solid-gauge'])

ui.highchart({
    'title': False,
    'rangeSelector': {'selected': 0},
    'series': [
        {'name': 'Gamma', 'data': [[1704067200000, 0.1], [1706745600000, 0.3], [1709251200000, 0.2]]},
    ],
}, type='stockChart', extras=['stock'])

ui.run(port=7777)
