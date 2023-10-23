from dataclasses import dataclass

from nicegui.dataclasses import KWONLY_SLOTS
from nicegui.events import UiEventArguments


@dataclass(**KWONLY_SLOTS)
class ChartEventArguments(UiEventArguments):
    event_type: str


@dataclass(**KWONLY_SLOTS)
class ChartPointClickEventArguments(ChartEventArguments):
    series_index: int
    point_index: int
    point_x: float
    point_y: float


@dataclass(**KWONLY_SLOTS)
class ChartPointDragStartEventArguments(ChartEventArguments):
    pass


@dataclass(**KWONLY_SLOTS)
class ChartPointDragEventArguments(ChartEventArguments):
    series_index: int
    point_index: int
    point_x: float
    point_y: float


@dataclass(**KWONLY_SLOTS)
class ChartPointDropEventArguments(ChartEventArguments):
    series_index: int
    point_index: int
    point_x: float
    point_y: float
