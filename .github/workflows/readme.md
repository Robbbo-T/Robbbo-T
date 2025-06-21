# GitHub Workflows

This directory contains the GitHub Actions workflows that automate various processes in our API Integration Strategy project.

## Overview

Our workflows are designed to maintain code quality, enforce standards, and streamline the development process for our API integration solutions.

## Workflows

### `main.yml`

The primary workflow that runs on every push to the main branch and on pull requests targeting main.

**Purpose:**
- Run tests across all integration strategy implementations
- Check code formatting and linting
- Build documentation
- Create package artifacts

**Trigger Events:**
- Push to `main` branch
- Pull requests to `main` branch

### `create-repo-structure.yml`

A utility workflow that helps maintain consistent repository structure across different API integration implementations.

**Purpose:**
- Generate standard directory structures for new integration strategies
- Create template files and boilerplate code
- Set up appropriate configuration files

**Trigger Events:**
- Manual trigger (`workflow_dispatch`)
- Repository creation

### `new-endpoint-checklist.yml`

Ensures all new API endpoints meet our quality standards and documentation requirements.

**Purpose:**
- Verify that new endpoints have appropriate tests
- Check for documentation completeness
- Validate OpenAPI/Swagger specifications
- Ensure cross-protocol compatibility

**Trigger Events:**
- Pull requests that add new API endpoints (detected via path filters)
- Manual trigger for verification

### `pull-request-check.yml`

Automates checking and solving pull requests.

**Purpose:**
- Run code linting
- Execute tests
- Check for merge conflicts
- Automatically add labels and comments based on the results of the checks
- Validate documentation
- Generate UI
- Generate technical reference documents
- Check for potential security issues and performance regressions
- Verify that new features or changes are well-documented

**Trigger Events:**
- Pull request creation and updates targeting the `main` branch

## Usage

### Running Workflows Manually

Some workflows can be triggered manually from the GitHub Actions tab:

1. Navigate to the "Actions" tab in the repository
2. Select the workflow you want to run
3. Click "Run workflow"
4. Select the branch and provide any required input parameters
5. Click "Run workflow" to start execution

### Workflow Status Badges

You can add workflow status badges to your documentation:

```markdown
![Main Workflow](https://github.com/Robbbo-T/api-integration-strategy/actions/workflows/main.yml/badge.svg)
![Endpoints Check](https://github.com/Robbbo-T/api-integration-strategy/actions/workflows/new-endpoint-checklist.yml/badge.svg)
![Pull Request Check](https://github.com/Robbbo-T/api-integration-strategy/actions/workflows/pull-request-check.yml/badge.svg)
```

## Customization

To modify existing workflows or add new ones:

1. Edit the YAML files in this directory
2. Follow [GitHub Actions syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
3. Test your changes in a branch before merging to main

## Best Practices

When working with these workflows:

- Don't modify workflow files directly in the main branch
- Test workflow changes in feature branches first
- Keep credentials and secrets secure using GitHub Secrets
- Document any new workflow steps added to existing workflows

## Troubleshooting

If a workflow fails:

1. Check the workflow run logs in the Actions tab
2. Verify that all required secrets and variables are properly set
3. Ensure your code meets the standards enforced by the workflows
4. Check for any GitHub Actions service disruptions

For persistent issues, please open an issue in the repository with the workflow run URL and description of the problem.
