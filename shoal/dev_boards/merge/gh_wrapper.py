"""GH CLI wrapper."""

import json
import shlex

import numpy as np
import pandas as pd
import pandera as pa
from beartype import beartype
from beartype.typing import Optional
from corallium.log import logger
from corallium.shell import capture_shell_async
from pandera.typing import Series

from .config import get_config


class PRsSchema(pa.SchemaModel):
    """Pandera Schema for the PRs DataFrame."""

    number: Series[str]
    repository: Series[str]
    title: Series[str]
    createdAt: Series[np.datetime64]  # noqa: N815
    updatedAt: Series[np.datetime64]  # noqa: N815
    commentsCount: Series[int]  # noqa: N815
    state: Series[str]  # = pa.Field(nullable=True)
    isDraft: Series[bool]  # noqa: N815
    isLocked: Series[bool]  # noqa: N815

    class Config:
        """Pandera Config."""

        strict = True
        coerce = True


PRColumns = [*PRsSchema._collect_fields()]  # noqa: SLF001
"""Ordered columns for the dataframe returned from `list_prs`."""


@beartype
@pa.check_output(PRsSchema)  # type: ignore[arg-type]
async def list_prs() -> pd.DataFrame:
    """Return a dataframe of all PRs."""
    config = get_config()
    gh_cli_args = []
    for key, value in config.search_kwargs.items():
        gh_cli_args += [f'--{key}', str(value)]
    joined_args = shlex.join(gh_cli_args)
    cmd = f"gh search prs --json='{','.join(PRColumns)}' --sort=updated --order=desc --limit=30 {joined_args}"
    output = await capture_shell_async(cmd)
    records = []
    for record in json.loads(output):
        repo = record.pop('repository')
        record[PRsSchema.repository] = repo['nameWithOwner']
        records.append({key: record[key] for key in PRColumns})
    df_prs = pd.DataFrame(records)
    return df_prs.sort_values(by=[PRsSchema.updatedAt], ascending=False)


@beartype
async def _safe_cmd(*, cmd: str) -> str:
    output = ''
    try:
        output = await capture_shell_async(cmd)
        logger.debug('Shell Output', cmd=cmd, output=output)
    except Exception:
        logger.exception('Error in command', cmd=cmd)
    return output


@beartype
async def open_pr(*, repository: str, pr_id: int) -> Optional[str]:
    """Open the PR using the GH CLi."""
    return await _safe_cmd(cmd=f"gh pr view {pr_id} --repo='{repository}' --web")


@beartype
async def merge_pr(*, repository: str, pr_id: int, use_squash: bool) -> Optional[str]:
    """Merge the PR."""
    opt_flags = '--squash' if use_squash else ''
    return await _safe_cmd(cmd=f"gh pr merge {pr_id} --repo='{repository}' --body='' {opt_flags}")
