"""A Textual Dashboard app for managing PRs."""

import logging
from itertools import cycle
from typing import Any, ClassVar

from beartype import beartype
from corallium.log import configure_logger
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.events import Mount
from textual.widgets import ContentSwitcher, DataTable, Footer, Header, RichLog

from .gh_wrapper import PRColumns, PRsSchema, list_prs, merge_pr, open_pr


@beartype
class DebugLog(RichLog):
    """Debug log widget."""

    DEFAULT_CSS = """
    #debug-log {
        dock: bottom;
        height: 10%;
    }
    """

    _text_logs = cycle(['debug-log', None])

    def compose(self) -> ComposeResult:
        super().compose()
        with ContentSwitcher(id='logs', initial=None):
            yield RichLog(id='debug-log', markup=True, highlight=True)

    # Override the logger to point to the debug-log
    def _app_printer(
        self,
        message: str,
        *,
        is_header: bool,
        _this_level: int,
        _is_text: bool,
        # Logger-specific parameters that need to be initialized with partial(...)
        **kwargs: Any,
    ) -> None:
        """App Log Writer."""
        values = ' '.join([f'{key}={value}' for key, value in kwargs.items()])
        log = self.query_one('#debug-log', RichLog)
        if is_header:
            log.write('')
        log.write(f'{message} {values}'.strip())

    def _on_mount(self, _: Mount) -> None:
        super()._on_mount(_)
        # Mount the logger to the debug log
        configure_logger(log_level=logging.DEBUG, logger=self._app_printer)

    def action_toggle_text_log(self) -> None:
        text_log_id = next(self._text_logs)
        new_id = self.query_one(f'#{text_log_id}', RichLog).id if text_log_id else None
        self.query_one('#logs', ContentSwitcher).current = new_id


@beartype
class PRsDataTable(DataTable):  # type: ignore[type-arg]
    """GitHub PRs Table."""

    _columns = PRColumns

    BINDINGS: ClassVar[list[Binding]] = [  # type: ignore[assignment]
        Binding('r', 'refresh_rows', 'Refresh Data'),
        Binding('o', 'open_selected_pr', 'Open in Browser'),
        Binding('m', 'merge_selected_pr', 'Merge'),
        Binding('s', 'squash_selected_pr', 'Squash'),
        Binding('k', 'cursor_up', 'Cursor Up', show=False),
        Binding('j', 'cursor_down', 'Cursor Down', show=False),
    ]

    def _get_selected_row(self) -> dict:  # type: ignore[type-arg]
        row = self.get_row_at(self.cursor_coordinate.row)
        return dict(zip(self._columns, row, strict=True))

    async def on_mount(self) -> None:
        super().on_mount()  # type: ignore[no-untyped-call]
        self.cursor_type = 'row'
        self.zebra_stripes = True
        self.add_columns(*self._columns)
        await self.action_refresh_rows()

    async def action_refresh_rows(self) -> None:
        self.clear()
        df_prs = await list_prs()
        self.add_rows(df_prs.itertuples(index=False))

    async def action_open_selected_pr(self) -> None:
        row_data = self._get_selected_row()
        await open_pr(repository=row_data[PRsSchema.repository], pr_id=row_data[PRsSchema.number])

    async def action_merge_selected_pr(self) -> None:
        row_data = self._get_selected_row()
        await merge_pr(repository=row_data[PRsSchema.repository], pr_id=row_data[PRsSchema.number], use_squash=False)

    async def action_squash_selected_pr(self) -> None:
        row_data = self._get_selected_row()
        await merge_pr(repository=row_data[PRsSchema.repository], pr_id=row_data[PRsSchema.number], use_squash=True)


@beartype
class MergeApp(App):  # type: ignore[type-arg]
    """A Textual Dashboard app for managing PRs."""

    TITLE = 'GitOps: Merge UI'

    BINDINGS: ClassVar[list[Binding]] = [  # type: ignore[assignment]
        Binding('q', 'quit', 'Quit'),
        Binding('`', 'toggle_text_log', 'Toggle Debug Log'),
        # PLANNED: Add question mark for a help menu
    ]

    def compose(self) -> ComposeResult:  # noqa: PLR6301
        """Called to add widgets to the app."""
        header = Header()
        header.tall = True
        yield header
        yield Footer()
        yield PRsDataTable(id='datatable')
        yield DebugLog()

    def _get_table(self) -> PRsDataTable:
        return self.query_one('#datatable', PRsDataTable)

    def action_toggle_text_log(self) -> None:
        self.query_one(DebugLog).action_toggle_text_log()


if __name__ == '__main__':
    MergeApp().run()
