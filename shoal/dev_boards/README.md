# `dev-boards`

Supports common workflows that are not tied to GitHub, Jira, or other tooling, but will only support those two at first

TLDR: Provide a constantly focused UI that only shows work that could be picked up, something that needs code review (PR + Ticket) or unassigned tickets that can be picked up, with minimal clutter

CLI commands of `dev-boards` or `brds`. Launches a tabbed TUI

- Tabs
    - Spike?: (timed) current focus
        - Show only what is currently being worked on
    - Shelf?: tasks pending external input (code review, designs, etc.)
    - Sprint: items for the current week
    - Queue: all planned work
    - Explore: general search across data sources
- Interactions
    - Move ticket between states, which stays in-sync with the external service
        - Would be useful to have custom rules that trigger on the state change, such as un-assigning or assigning, etc., but would be better to have generic keyboard shortcuts that make these tasks easy
    - Provide a quick preview of the content
    - Support micro-interactions, like leaving comments

## Other

- Iterate through and delete all log output from an Action? Previous bash snippet below

```sh
# GitHub API docs: https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2022-11-28
#   GH CLI Docs: https://cli.github.com/manual/gh_api
# Inspiration: https://qmacro.org/blog/posts/2021/03/26/mass-deletion-of-github-actions-workflow-runs/

OWNER=kyleking
WORKFLOW_ID=upgrade-dependencies.yml

# for repo in $(gh repo list --json="name" --jq=".[].name"); do
for repo in $(echo -e "cz_legacy\npersonal-man\nextract_finances"); do
    echo "Checking $repo"
    run_ids=$( \
        gh api \
        --header "Accept: application/vnd.github+json" \
        --header "X-GitHub-Api-Version: 2022-11-28" \
        "/repos/$OWNER/$repo/actions/workflows/$WORKFLOW_ID/runs" \
        --method=GET \
        --raw-field='per_page=100' \
        --jq '.workflow_runs[].id' \
    )
    echo $run_ids | xargs -I+ echo +
    echo $run_ids | xargs -I+ gh api -X DELETE "/repos/$OWNER/$repo/actions/runs/+"
done
```
