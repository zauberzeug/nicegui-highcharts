from dataclasses import dataclass

from nicegui.events import UiEventArguments


@dataclass(kw_only=True, slots=True)
class ChartEventArguments(UiEventArguments):
    event_type: str


@dataclass(kw_only=True, slots=True)
class ChartPointClickEventArguments(ChartEventArguments):
    series_index: int
    point_index: int
    point_x: float
    point_y: float


@dataclass(kw_only=True, slots=True)
class ChartPointDragStartEventArguments(ChartEventArguments):
    pass


@dataclass(kw_only=True, slots=True)
class ChartPointDragEventArguments(ChartEventArguments):
    series_index: int
    point_index: int
    point_x: float
    point_y: float


@dataclass(kw_only=True, slots=True)
class ChartPointDropEventArguments(ChartEventArguments):
    series_index: int
    point_index: int
    point_x: float
    point_y: float
