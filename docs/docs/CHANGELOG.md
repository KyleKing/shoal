## Unreleased

### Fix

- final commit. Moving all logic into calcipy

## 1.0.0rc0 (2023-02-21)

### Feat

- add type annotations and fix linting issues
- upgrade to calcipy v1 with copier

### Fix

- use regex for commitizen versioning
- remove pyright venvPath
- don't remove binary name from sys.argv. Run calcipy!
- default verbose should be 1

### Refactor

- rename shell( to run_shell( and update docs
- resolve type errors

## 0.6.0 (2023-02-20)

### Feat

- support working-dir
- add logger.print and print_debug

## 0.5.1 (2023-02-19)

### Fix

- correct return from can_skip & one-line summary

## 0.5.0 (2023-02-18)

### Fix

- correct mtime comparison in can_skip

### Refactor

- remove shoaling/tangs and top-level imports

## 0.4.1 (2023-02-17)

### Fix

- can_skip, logging, and type cli.task

## 0.4.0 (2023-02-17)

### Feat

- wrap the invoke task
- add invoke program wrappers from Calcipy

### Refactor

- use prerequisites for consistency

## 0.3.0 (2023-02-09)

### Feat

- add pretty_process
- add can_skip from calcipy

### Fix

- add missing configure_logger

## 0.2.1 (2023-02-08)

### Fix

- remove dependency on calcipy, reduce public interface, and more log-like

## 0.2.0 (2023-02-07)

### Feat

- add debug logging
- add intermediary pydantic model for argparser
- add logger
- add register_fun

### Refactor

- reorganize and add a timeout

## 0.1.0 (2023-02-06)

### Feat

- finish first proof of concept
- initialize Tang model
- initialize with copier

### Refactor

- run doit against all files
