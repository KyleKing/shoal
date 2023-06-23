# Actions

Static analysis and fixers for GitHub Actions

<!-- TODO: Implement -->

- Checks inputs/outputs of remote workflows by caching the `yaml` file
- Reads the YAML files by replacing all evaluated sections with a unique string and database lookup
- Shows warnings on `snake_case` attributes, and can auto-fix them
- No per-line ignores, but can ignore the `snake_case` check (VAR01, KEB01, SNK01 for the inverse, or something like that) globally
- For format, use `prettier`. For general linting, use [`actionlint`](https://github.com/rhysd/actionlint)

---

## Action Checker

Pre-GH-Ops notes:

- download file from GitHub API at specified tag (Only checks 1-deep)
    - cached in repo/file path/version globally
    - has TTL per file and knows when path is relative
    - Used to check arguments, identify missing required, and unknown
- can document external actions in summary.Md that uses descriptions, input/outputs, list of internally used versions, and latest tag. All shown in a table with the header being a direct link
    - Can be used for internal reference and/or external documentation
- Can be run in pre-commit or GitHub Action
    - Needs user’s API token for access to private repos and to avoid GH API rate limits
- should encapsulate logic specific to GitHub Actions behind BaseModels
- Based on ruff and isort. Provides named rules that have a corresponding id and can be ignored with `# noac: <>` (No ActionChecker). Need to decide on supporting inline, above-line, CLI, and/or configuration file
- Could check for proper use of context (i.e. vars in env, but not in with), env in other places, etc. but probably not worthwhile
