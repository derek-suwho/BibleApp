# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

BibleApp is a Python-based web application for Bible study and reading. The project uses traditional web technologies (HTML/JavaScript) with a SQL database backend and Elasticsearch for search functionality.

## Tech Stack

- **Backend**: Python web application
- **Frontend**: HTML/JavaScript (simple, not a complex framework)
- **Database**: SQL databases (separate for dev, test, and prod environments)
- **Search**: Elasticsearch hosted on elastic.co (dev and prod indexes)
- **Testing**: Python tests

## Development Philosophy

### Code Quality Standards
- Keep files under 200-300 lines
- Prefer simple solutions over complex ones
- Avoid code duplication
- Maintain clean, organized codebase
- Focus on task-relevant code only

### Environment Management
- Use environment-aware code (dev/test/prod)
- Separate databases for each environment
- Never overwrite .env files without explicit confirmation
- No mocking in dev/prod environments (only in tests)

### Development Approach
- Conservative changes - avoid major architectural modifications once features work well
- Thorough testing for major functionality
- Consider impact on other code areas when making changes
- No JSON file storage - use SQL databases

## Architecture Notes

### Multi-Environment Setup
The application is designed to work across three environments:
- **Development**: Local development with dev database and search index
- **Test**: Testing environment with isolated test database
- **Production**: Live environment with prod database and search index

### Search Implementation
- Elasticsearch hosted on elastic.co
- Separate indexes for development and production
- Search functionality integrated with Bible text and study features

## Development Workflow

When working on this codebase:
1. Always consider which environment your changes affect
2. Write tests for major functionality changes
3. Keep changes focused and avoid unnecessary architectural modifications
4. Ensure database queries work across all environments
5. Test search functionality against appropriate Elasticsearch indexes