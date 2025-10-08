from typing import Callable, Optional

from nicegui import events, ui

from .events import (
    ChartPointClickEventArguments,
    ChartPointDragEventArguments,
    ChartPointDragStartEventArguments,
    ChartPointDropEventArguments,
)


class Highchart(ui.element, component='highchart.js', esm={'nicegui-highcharts': 'dist'}):

    def __init__(self, options: dict, *,
                 type: str = 'chart', extras: list[str] = [],  # noqa: B006  # pylint: disable=redefined-builtin
                 on_point_click: Optional[Callable] = None,
                 on_point_drag_start: Optional[Callable] = None,
                 on_point_drag: Optional[Callable] = None,
                 on_point_drop: Optional[Callable] = None,
                 ) -> None:
        """Highcharts chart

        An element to create a chart using `Highcharts <https://www.highcharts.com/>`_.
        Updates can be pushed to the chart by changing the `options` property.
        After data has changed, call the `update` method to refresh the chart.

        Due to Highcharts' restrictive license, this element is not part of the standard NiceGUI package.
        It is maintained in a `separate repository <https://github.com/zauberzeug/nicegui-highcharts/>`_
        and can be installed with `pip install nicegui[highcharts]`.

        By default, a `Highcharts.chart` is created.
        To use, e.g., `Highcharts.stockChart` instead, set the `type` property to "stockChart".

        :param options: dictionary of Highcharts options
        :param type: chart type (e.g. "chart", "stockChart", "mapChart", ...; default: "chart")
        :param extras: list of extra dependencies to include (e.g. "annotations", "arc-diagram", "solid-gauge", ...)
        :param on_point_click: callback function that is called when a point is clicked
        :param on_point_drag_start: callback function that is called when a point drag starts
        :param on_point_drag: callback function that is called when a point is dragged
        :param on_point_drop: callback function that is called when a point is dropped
        """
        super().__init__()
        self._props['type'] = type
        self._props['options'] = options
        self._props['extras'] = extras

        if on_point_click:
            def handle_point_click(e: events.GenericEventArguments) -> None:
                events.handle_event(on_point_click, ChartPointClickEventArguments(
                    sender=self,
                    client=self.client,
                    event_type='point_click',
                    point_index=e.args['point_index'],
                    point_x=e.args['point_x'],
                    point_y=e.args['point_y'],
                    series_index=e.args['series_index'],
                ))
            self.on('pointClick', handle_point_click, ['point_index', 'point_x', 'point_y', 'series_index'])

        if on_point_drag_start:
            def handle_point_dragStart(_: events.GenericEventArguments) -> None:
                events.handle_event(on_point_drag_start, ChartPointDragStartEventArguments(
                    sender=self,
                    client=self.client,
                    event_type='point_drag_start',
                ))
            self.on('pointDragStart', handle_point_dragStart, [])

        if on_point_drag:
            def handle_point_drag(e: events.GenericEventArguments) -> None:
                events.handle_event(on_point_drag, ChartPointDragEventArguments(
                    sender=self,
                    client=self.client,
                    event_type='point_drag',
                    point_index=e.args['point_index'],
                    point_x=e.args['point_x'],
                    point_y=e.args['point_y'],
                    series_index=e.args['series_index'],
                ))
            self.on('pointDrag', handle_point_drag, ['point_index', 'point_x', 'point_y', 'series_index'])

        if on_point_drop:
            def handle_point_drop(e: events.GenericEventArguments) -> None:
                events.handle_event(on_point_drop, ChartPointDropEventArguments(
                    sender=self,
                    client=self.client,
                    event_type='point_drop',
                    point_index=e.args['point_index'],
                    point_x=e.args['point_x'],
                    point_y=e.args['point_y'],
                    series_index=e.args['series_index'],
                ))
            self.on('pointDrop', handle_point_drop, ['point_index', 'point_x', 'point_y', 'series_index'])

    @property
    def options(self) -> dict:
        """The options dictionary."""
        return self._props['options']

    def update(self) -> None:
        super().update()
        self.run_method('update_chart')
