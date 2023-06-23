# PR Merge

- Lists all PRs created by me, which are ready to be merged
- Collects these PRs using a properly configure GH CLI
- Shows the PR ID, repo, dates, and title. Optionally displays the body text?
- Per PR, offers to `o` open in the browser for manual review, `m` merge, `s` squash, etc.
    - Uses environment branch rules to determine if squash or merge is preferred, then raise warning if one or the other was actually intended

## What should it actually do...

- Show latest deployed branch per environment?
- Allow easier selection of workflows to run and options? (Or make that a separate script that can partially parse action files for the arguments (and choices)?)
    - Maybe just `fzf` for quick select of prepared bash statements?
- Can get PR ID from branches: `export repo=$(gh repo view --json nameWithOwner -q ".nameWithOwner") && export pr_number=$(gh search prs --repo=$repo --state=open --json='number' -- head:branch-source base:branch-target | jq ".[].number")` then if non-empty, you have a PR number
