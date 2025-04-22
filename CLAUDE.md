# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build, Lint & Test Commands
- Start dev environment: `hatch run dev`
- Run all tests: `hatch run test`
- Run single test: `hatch run test tests/test_specific.py::test_function_name`
- Lint code: `hatch run lint`
- Type check: `hatch run type`
- Format code: `hatch run format`
- Docker commands: `hatch run docker-up`, `hatch run docker-down`, `hatch run docker-logs`

## Code Style Guidelines
- **Imports**: Standard library first, then third-party, then local (sorted alphabetically)
- **Formatting**: 88 char line length, double quotes, space indentation
- **Types**: Strong typing with mypy, explicit return types, all functions must have type hints
- **Naming**: PascalCase for classes, snake_case for functions/variables, UPPER_SNAKE_CASE for constants
- **Error Handling**: Use explicit HTTP exceptions with detailed error messages
- **Documentation**: Google-style docstrings with detailed API documentation
- **Testing**: Use pytest with pytest-asyncio, include happy paths and error cases

Always run `hatch run type` and `hatch run lint` after making changes to verify code quality.

## Additional Guidelines
- Always read the AI.md file for preferred coding standards
- Create and update TODO.md with action items as instructions are received