# Git, GitHub & CI/CD: Complete Learning Guide for DevOps Beginners

> **A comprehensive guide covering Git version control, GitHub collaboration, and CI/CD automation for development teams**

## Table of Contents

1. [Introduction to Git & GitHub](#introduction-to-git--github)
2. [Version Control with Git](#version-control-with-git)
3. [Common Git Commands](#common-git-commands)
4. [What is CI/CD and Why It Matters](#what-is-cicd-and-why-it-matters)
5. [Basic CI/CD Workflow](#basic-cicd-workflow)
6. [Setting Up CI/CD with GitHub Actions](#setting-up-cicd-with-github-actions)
7. [Build-Test-Deploy Process](#build-test-deploy-process)
8. [Best Practices](#best-practices)
9. [Troubleshooting Guide](#troubleshooting-guide)
10. [Additional Resources](#additional-resources)

---

## Introduction to Git & GitHub

### What is Git?

Git is a distributed version control system (DVCS) that allows developers to track and manage changes to their codebase. Unlike traditional version control systems, Git allows multiple developers to work on a project simultaneously without interfering with each other's work.

### What is GitHub?

GitHub is a company founded in 2008 that makes tools which integrate with git. You do not need GitHub to use git, but you cannot use GitHub without using git. GitHub provides:

- **Remote Repositories**: Cloud-based storage for your Git repositories
- **Collaboration Tools**: Pull requests, issues, and project management
- **CI/CD Integration**: GitHub Actions for automation
- **Documentation**: README files, wikis, and GitHub Pages

### Git vs GitHub Comparison

| Feature | Git | GitHub |
|---------|-----|--------|
| **Type** | Version control system | Cloud-based hosting service |
| **Purpose** | Track code changes locally | Remote collaboration & storage |
| **Installation** | Requires local installation | Web-based service |
| **Collaboration** | Basic (via remote repos) | Advanced (PRs, issues, discussions) |
| **Cost** | Free & open source | Free tier + paid plans |

### Git Workflow Overview

```mermaid
gitgraph
    commit id: "Initial"
    commit id: "Feature A"
    branch develop
    checkout develop
    commit id: "Dev Setup"
    branch feature/login
    checkout feature/login
    commit id: "Add login"
    commit id: "Add validation"
    checkout develop
    merge feature/login
    commit id: "Integration"
    checkout main
    merge develop
    commit id: "Release v1.0"
```

---

## Version Control with Git

### Core Concepts

**Version control** is a system that records changes to files over time so you can recall specific versions later. Git uses a distributed model where every developer has a complete copy of the project history.

### The Three States of Git

Your local repository consists of three "trees" maintained by git. The first one is your Working Directory which holds the actual files. The second one is the Index which acts as a staging area and finally the HEAD which points to the last commit you've made.

```mermaid
graph LR
    A[Working Directory] -->|git add| B[Staging Area]
    B -->|git commit| C[Repository]
    C -->|git push| D[Remote Repository]
    D -->|git pull| A
```

### Git Repository Structure

```
project-folder/
├── .git/                 # Git metadata (hidden)
├── .gitignore           # Files to ignore
├── README.md            # Project documentation
├── src/                 # Source code
├── tests/               # Test files
└── docs/                # Documentation
```

### Understanding Branches

Branches are used to develop features isolated from each other. The main branch is the "default" branch when you create a repository.

**Main Branch Types:**
- **main/master**: Production-ready code
- **develop**: Integration branch for features
- **feature**: New feature development
- **release**: Preparing new releases
- **hotfix**: Emergency bug fixes

```mermaid
gitgraph
    commit id: "v1.0"
    branch develop
    checkout develop
    commit id: "Setup"
    
    branch feature/navbar
    checkout feature/navbar
    commit id: "Add navbar"
    commit id: "Style navbar"
    
    checkout develop
    merge feature/navbar
    
    branch feature/footer
    checkout feature/footer
    commit id: "Add footer"
    
    checkout develop
    merge feature/footer
    commit id: "Integration test"
    
    checkout main
    merge develop
    commit id: "v1.1"
    
    branch hotfix/bug-123
    checkout hotfix/bug-123
    commit id: "Fix critical bug"
    
    checkout main
    merge hotfix/bug-123
    commit id: "v1.1.1"
    
    checkout develop
    merge hotfix/bug-123
```

---

## Common Git Commands

### Essential Commands Table

| Command | Purpose | Example |
|---------|---------|---------|
| `git init` | Initialize repository | `git init my-project` |
| `git clone` | Copy remote repository | `git clone https://github.com/user/repo.git` |
| `git add` | Stage changes | `git add .` or `git add filename.js` |
| `git commit` | Save changes | `git commit -m "Add new feature"` |
| `git push` | Upload changes | `git push origin main` |
| `git pull` | Download changes | `git pull origin main` |
| `git status` | Check repository status | `git status` |
| `git log` | View commit history | `git log --oneline` |

### 1. Repository Setup

```bash
# Initialize a new repository
git init

# Clone existing repository
git clone https://github.com/username/repository-name.git

# Add remote origin
git remote add origin https://github.com/username/repo.git
```

### 2. Basic Workflow Commands

```bash
# Check current status
git status

# Add files to staging area
git add .                    # Add all files
git add src/index.js         # Add specific file
git add src/                 # Add specific directory

# Commit changes
git commit -m "Descriptive commit message"

# Push to remote repository
git push origin main         # Push to main branch
git push origin feature-name # Push to feature branch

# Pull latest changes
git pull origin main
```

### 3. Branch Management

```bash
# List branches
git branch                   # Local branches
git branch -r               # Remote branches
git branch -a               # All branches

# Create and switch to new branch
git checkout -b feature/user-authentication
git switch -c feature/user-authentication  # Modern alternative

# Switch between branches
git checkout main
git switch develop          # Modern alternative

# Merge branches
git checkout main
git merge feature/user-authentication

# Delete branch
git branch -d feature/user-authentication    # Safe delete
git branch -D feature/user-authentication    # Force delete
```

### 4. Advanced Commands

```bash
# View commit history
git log --oneline --graph --all

# Show differences
git diff                     # Unstaged changes
git diff --staged           # Staged changes
git diff HEAD~1             # Compare with previous commit

# Stash changes temporarily
git stash                   # Save current changes
git stash pop              # Restore stashed changes
git stash list             # View all stashes

# Reset and revert
git reset HEAD~1           # Undo last commit (keep changes)
git reset --hard HEAD~1    # Undo last commit (discard changes)
git revert HEAD            # Create new commit that undoes changes
```

### Git Configuration

```bash
# Set global configuration
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main

# View configuration
git config --list
git config user.name

# Set up SSH key (recommended)
ssh-keygen -t ed25519 -C "your.email@example.com"
```

---

## What is CI/CD and Why It Matters

### Definition

CI/CD stands for Continuous Integration and Continuous Deployment (or Continuous Delivery). It's a set of practices and tools designed to improve the software development process by automating builds, testing, and deployment, enabling you to ship code changes faster and reliably.

### CI/CD Components

```mermaid
graph TD
    A[Developer Commits Code] --> B[Continuous Integration]
    B --> C{Automated Tests Pass?}
    C -->|Yes| D[Build Artifact]
    C -->|No| E[Notify Developer]
    E --> A
    D --> F[Continuous Delivery]
    F --> G[Deploy to Staging]
    G --> H{Manual Approval?}
    H -->|Yes| I[Continuous Deployment]
    H -->|No| J[Hold for Review]
    I --> K[Deploy to Production]
    J --> H
```

### Continuous Integration (CI)

Automatically builds, tests, and integrates code changes within a shared repository

**Key Features:**
- **Automated Testing**: Run unit, integration, and security tests
- **Build Automation**: Compile and package code automatically
- **Code Quality Checks**: Linting, formatting, and static analysis
- **Early Bug Detection**: Catch issues before they reach production

### Continuous Delivery vs Deployment

| Continuous Delivery | Continuous Deployment |
|---------------------|----------------------|
| **Manual approval** required for production | **Fully automated** to production |
| **Human oversight** for releases | **No human intervention** |
| **Safer** for critical systems | **Faster** time to market |
| **Better for compliance** requirements | **Ideal for** web applications |

### Why CI/CD Matters

**Benefits for Development Teams:**

1. **Faster Time to Market**
   - Accelerate software delivery and detect vulnerabilities and bugs earlier
   - Reduce manual deployment time from hours to minutes

2. **Improved Code Quality**
   - Automated testing catches bugs early
   - Consistent code standards enforcement
   - Reduced human error in deployments

3. **Enhanced Collaboration**
   - Treating code review as a best practice improves code quality, encourages collaboration, and helps even the most experienced developers make better commits
   - Transparent development process
   - Better visibility into project status

4. **Risk Reduction**
   - Smaller, frequent deployments
   - Easy rollback capabilities
   - Consistent deployment environments

**Industry Impact:**
- According to GitLab's 2024 Global DevSecOps report, continuous integration, deployment, and delivery is among the top IT investment priorities in 2023 and 2024, ranking 8th place

---

## Basic CI/CD Workflow

### Standard CI/CD Pipeline

```mermaid
graph LR
    A[Code Commit] --> B[Trigger CI]
    B --> C[Install Dependencies]
    C --> D[Run Tests]
    D --> E{Tests Pass?}
    E -->|No| F[Notify Developer]
    E -->|Yes| G[Build Application]
    G --> H[Security Scan]
    H --> I[Deploy to Staging]
    I --> J[Integration Tests]
    J --> K{Ready for Production?}
    K -->|No| L[Manual Review]
    K -->|Yes| M[Deploy to Production]
    L --> K
```

### Workflow Stages Explained

#### 1. Source Stage
- Developer commits code to version control
- Webhook triggers the pipeline
- Code is checked out to build environment

#### 2. Build Stage
- **Install Dependencies**: Download required packages
- **Compile Code**: Transform source code into executable format
- **Run Static Analysis**: Check code quality and security
- **Create Artifacts**: Package the application

#### 3. Test Stage
- **Unit Tests**: Test individual components
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete user workflows
- **Security Tests**: Vulnerability scanning

#### 4. Deploy Stage
- **Staging Deployment**: Deploy to testing environment
- **Smoke Tests**: Basic functionality verification
- **Performance Tests**: Load and stress testing
- **Production Deployment**: Release to users

### CI/CD Pipeline Configuration

#### Pipeline Triggers

| Trigger Type | When It Runs | Use Case |
|--------------|--------------|----------|
| **Push** | Code pushed to repository | Basic CI on every change |
| **Pull Request** | PR created or updated | Code review and testing |
| **Schedule** | Time-based (cron) | Nightly builds, security scans |
| **Manual** | User-initiated | Production deployments |
| **Tag** | Git tag created | Release deployments |

#### Environment Strategy

```mermaid
graph TD
    A[Development] --> B[Testing/Staging]
    B --> C[Pre-production]
    C --> D[Production]
    
    A1[Feature Branches] --> A
    B1[Integration Tests] --> B
    C1[User Acceptance] --> C
    D1[Live Users] --> D
```

**Environment Characteristics:**

| Environment | Purpose | Deployment | Testing |
|-------------|---------|------------|---------|
| **Development** | Feature development | Automatic on push | Unit tests |
| **Testing/Staging** | Integration testing | Automatic on PR merge | Integration & E2E tests |
| **Pre-production** | Final validation | Manual approval | User acceptance testing |
| **Production** | Live application | Manual/scheduled | Monitoring & health checks |

---

## Setting Up CI/CD with GitHub Actions

### Introduction to GitHub Actions

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that automates build, test, and deployment pipelines. It allows you to create workflows that build and test every pull request to your repository, or deploy merged pull requests to your production environment.

### Key Advantages

GitHub Actions has several key benefits:

- **CI/CD pipeline set-up is simple**: You just drop one file in your repo, and it works
- **Respond to any webhook on GitHub**: Set any webhook as an event trigger for automation
- **Community-powered, reusable workflows**: Access pre-built CI/CD workflows in the GitHub Marketplace (there are more than 11,000 available actions!)
- **Support for any platform, any language, and any cloud**: GitHub Actions is platform agnostic, language agnostic, and cloud agnostic

### Basic Workflow Structure

GitHub Actions workflows are defined in YAML files stored in `.github/workflows/` directory.

```yaml
name: CI/CD Pipeline                    # Workflow name
on: [push, pull_request]               # Triggers
jobs:                                  # Jobs to run
  test:                               # Job name
    runs-on: ubuntu-latest            # Runner environment
    steps:                            # Steps to execute
      - uses: actions/checkout@v4     # Action to use
      - name: Setup Node.js           # Step name
        uses: actions/setup-node@v4   # Action
        with:                         # Action parameters
          node-version: '18'
      - run: npm install              # Command to run
      - run: npm test                 # Another command
```

### Essential GitHub Actions Components

#### 1. Events (Triggers)

```yaml
# Single event
on: push

# Multiple events
on: [push, pull_request]

# Event with conditions
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
    
# Scheduled event
on:
  schedule:
    - cron: '0 2 * * *'  # Run daily at 2 AM UTC
```

#### 2. Jobs and Runners

```yaml
jobs:
  build:
    runs-on: ubuntu-latest        # GitHub-hosted runner
    
  test:
    runs-on: windows-latest       # Windows runner
    
  deploy:
    runs-on: self-hosted          # Self-hosted runner
    needs: [build, test]          # Dependencies
```

#### 3. Steps and Actions

```yaml
steps:
  # Use existing action
  - uses: actions/checkout@v4
  
  # Run shell command
  - run: echo "Hello World"
  
  # Named step with action
  - name: Setup Python
    uses: actions/setup-python@v4
    with:
      python-version: '3.9'
  
  # Multi-line script
  - name: Run tests
    run: |
      python -m pytest
      python -m coverage report
```

### Complete Example: Node.js Application

```yaml
name: Node.js CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  NODE_VERSION: '18'

jobs:
  test:
    name: Test Application
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Run linter
      run: npm run lint
      
    - name: Run tests
      run: npm test
      
    - name: Upload coverage reports
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage/lcov.info

  build:
    name: Build Application
    runs-on: ubuntu-latest
    needs: test
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Build application
      run: npm run build
      
    - name: Upload build artifacts
      uses: actions/upload-artifact@v3
      with:
        name: build-files
        path: dist/

  deploy:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: [test, build]
    if: github.ref == 'refs/heads/main'
    environment: production
    
    steps:
    - name: Download build artifacts
      uses: actions/download-artifact@v3
      with:
        name: build-files
        
    - name: Deploy to server
      run: |
        echo "Deploying to production server..."
        # Your deployment commands here
```

### Matrix Builds

Matrix builds in continuous integration allow you to automatically run tests across various combinations of operating systems and programming language versions.

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [16, 18, 20]
        
    steps:
    - uses: actions/checkout@v4
    - name: Setup Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm ci
    - run: npm test
```

### Working with Secrets

GitHub Secrets allow you to store sensitive information securely.

#### Setting Up Secrets

1. Go to your repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add your secret name and value

#### Using Secrets in Workflows

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to AWS
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      run: |
        aws s3 sync ./build s3://my-bucket
```

### Environment Protection

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: 
      name: production
      url: https://myapp.com
    steps:
    - name: Deploy application
      run: echo "Deploying to production"
```

---

## Build-Test-Deploy Process

### Overview of the Process

The Build-Test-Deploy process is the core of CI/CD automation that ensures code quality and reliable deployments.

```mermaid
graph TD
    A[Source Code] --> B[Build Stage]
    B --> C[Test Stage]
    C --> D[Deploy Stage]
    
    B1[Install Dependencies] --> B
    B2[Compile/Transpile] --> B
    B3[Bundle Assets] --> B
    B4[Create Artifacts] --> B
    
    C1[Unit Tests] --> C
    C2[Integration Tests] --> C
    C3[Security Scans] --> C
    C4[Quality Gates] --> C
    
    D1[Deploy to Staging] --> D
    D2[Smoke Tests] --> D
    D3[Deploy to Production] --> D
    D4[Health Checks] --> D
```

### 1. Build Stage

The build stage transforms your source code into deployable artifacts.

#### Node.js Build Example

```yaml
build:
  name: Build Application
  runs-on: ubuntu-latest
  steps:
  - name: Checkout code
    uses: actions/checkout@v4
    
  - name: Setup Node.js
    uses: actions/setup-node@v4
    with:
      node-version: '18'
      cache: 'npm'
      
  - name: Install dependencies
    run: npm ci
    
  - name: Build application
    run: npm run build
    
  - name: Create build info
    run: |
      echo "Build Date: $(date)" > dist/build-info.txt
      echo "Commit: ${{ github.sha }}" >> dist/build-info.txt
      echo "Branch: ${{ github.ref_name }}" >> dist/build-info.txt
      
  - name: Upload artifacts
    uses: actions/upload-artifact@v3
    with:
      name: production-build
      path: dist/
      retention-days: 30
```

#### Docker Build Example

```yaml
build-docker:
  name: Build Docker Image
  runs-on: ubuntu-latest
  steps:
  - name: Checkout code
    uses: actions/checkout@v4
    
  - name: Set up Docker Buildx
    uses: docker/setup-buildx-action@v2
    
  - name: Login to Docker Hub
    uses: docker/login-action@v2
    with:
      username: ${{ secrets.DOCKER_USERNAME }}
      password: ${{ secrets.DOCKER_PASSWORD }}
      
  - name: Build and push
    uses: docker/build-push-action@v4
    with:
      context: .
      push: true
      tags: myapp:${{ github.sha }},myapp:latest
      cache-from: type=gha
      cache-to: type=gha,mode=max
```

### 2. Test Stage

Comprehensive testing ensures code quality and functionality.

#### Testing Strategy

| Test Type | Purpose | When to Run | Example Tools |
|-----------|---------|-------------|---------------|
| **Unit Tests** | Test individual functions | Every commit | Jest, pytest, JUnit |
| **Integration Tests** | Test component interactions | PR merge | Supertest, TestNG |
| **E2E Tests** | Test user workflows | Before deployment | Cypress, Playwright |
| **Security Tests** | Find vulnerabilities | Daily/Weekly | OWASP ZAP, Snyk |
| **Performance Tests** | Check speed/load | Before release | JMeter, Lighthouse |

#### Complete Test Pipeline

```yaml
test:
  name: Run Tests
  runs-on: ubuntu-latest
  services:
    postgres:
      image: postgres:13
      env:
        POSTGRES_PASSWORD: postgres
      options: >-
        --health-cmd pg_isready
        --health-interval 10s
        --health-timeout 5s
        --health-retries 5
        
  steps:
  - name: Checkout code
    uses: actions/checkout@v4
    
  - name: Setup Node.js
    uses: actions/setup-node@v4
    with:
      node-version: '18'
      cache: 'npm'
      
  - name: Install dependencies
    run: npm ci
    
  - name: Run linting
    run: npm run lint
    
  - name: Run unit tests
    run: npm run test:unit
    env:
      NODE_ENV: test
      DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test
      
  - name: Run integration tests
    run: npm run test:integration
    
  - name: Generate test coverage
    run: npm run test:coverage
    
  - name: Upload coverage to Codecov
    uses: codecov/codecov-action@v3
    with:
      file: ./coverage/lcov.info
      fail_ci_if_error: true
      
  - name: Security audit
    run: npm audit --audit-level moderate
    
  - name: Dependency check
    uses: actions/dependency-review-action@v3
```

#### Quality Gates

Quality gates prevent poor code from reaching production:

```yaml
quality-gate:
  name: Quality Gate
  runs-on: ubuntu-latest
  needs: test
  steps:
  - name: Check test coverage
    run: |
      COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
      if (( $(echo "$COVERAGE < 80" | bc -l) )); then
        echo "Coverage $COVERAGE% is below 80% threshold"
        exit 1
      fi
      echo "Coverage $COVERAGE% meets threshold"
      
  - name: Check for vulnerabilities
    run: |
      if npm audit --audit-level high --json | jq '.vulnerabilities | length' | grep -v '^0$'; then
        echo "High severity vulnerabilities found"
        exit 1
      fi
```

### 3. Deploy Stage

Deployment stage releases your application to various environments.

#### Deployment Strategy

```mermaid
graph LR
    A[Build Artifacts] --> B{Environment}
    B -->|Feature Branch| C[Development]
    B -->|Pull Request| D[Preview]
    B -->|Develop Branch| E[Staging]
    B -->|Main Branch| F[Production]
    
    C --> C1[Auto Deploy]
    D --> D1[Auto Deploy]
    E --> E1[Auto Deploy]
    F --> F1[Manual Approval]
    F1 --> F2[Blue-Green Deploy]
```

#### Multi-Environment Deployment

```yaml
deploy-staging:
  name: Deploy to Staging
  runs-on: ubuntu-latest
  needs: [build, test]
  if: github.ref == 'refs/heads/develop'
  environment:
    name: staging
    url: https://staging.myapp.com
    
  steps:
  - name: Download artifacts
    uses: actions/download-artifact@v3
    with:
      name: production-build
      
  - name: Deploy to staging
    run: |
      echo "Deploying to staging environment..."
      # Your staging deployment commands
      
  - name: Run smoke tests
    run: |
      curl -f https://staging.myapp.com/health || exit 1
      echo "Staging deployment successful"

deploy-production:
  name: Deploy to Production
  runs-on: ubuntu-latest
  needs: [build, test, deploy-staging]
  if: github.ref == 'refs/heads/main'
  environment:
    name: production
    url: https://myapp.com
    
  steps:
  - name: Download artifacts
    uses: actions/download-artifact@v3
    with:
      name: production-build
      
  - name: Blue-Green Deployment
    run: |
      echo "Starting blue-green deployment..."
      # Deploy to green environment
      # Run health checks
      # Switch traffic from blue to green
      # Keep blue as rollback option
      
  - name: Post-deployment verification
    run: |
      curl -f https://myapp.com/health || exit 1
      echo "Production deployment successful"
      
  - name: Notify team
    uses: 8398a7/action-slack@v3
    with:
      status: ${{ job.status }}
      channel: '#deployments'
      webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

#### Deployment Patterns

**Blue-Green Deployment:**
```yaml
blue-green-deploy:
  steps:
  - name: Deploy to Green Environment
    run: |
      # Deploy new version to green environment
      docker run -d --name myapp-green myapp:${{ github.sha }}
      
  - name: Health Check Green
    run: |
      # Verify green environment is healthy
      ./scripts/health-check.sh green
      
  - name: Switch Traffic
    run: |
      # Switch load balancer to green
      ./scripts/switch-traffic.sh green
      
  - name: Cleanup Blue
    run: |
      # Keep blue for quick rollback, cleanup later
      sleep 300  # Wait 5 minutes
      docker stop myapp-blue
```

**Rolling Deployment:**
```yaml
rolling-deploy:
  strategy:
    matrix:
      server: [server1, server2, server3]
  steps:
  - name: Deploy to ${{ matrix.server }}
    run: |
      # Deploy to one server at a time
      ssh ${{ matrix.server }} 'docker pull myapp:${{ github.sha }}'
      ssh ${{ matrix.server }} 'docker stop myapp || true'
      ssh ${{ matrix.server }} 'docker run -d --name myapp myapp:${{ github.sha }}'
```

### Monitoring and Observability

Post-deployment monitoring ensures your application is running correctly:

```yaml
post-deploy-monitoring:
  name: Post-Deployment Monitoring
  runs-on: ubuntu-latest
  needs: deploy-production
  steps:
  - name: Setup monitoring
    run: |
      # Enable application metrics
      curl -X POST https://myapp.com/admin/enable-metrics
      
  - name: Verify key metrics
    run: |
      # Check response time, error rate, throughput
      ./scripts/check-metrics.sh
      
  - name: Create deployment marker
    run: |
      # Mark deployment in monitoring system
      curl -X POST "https://api.datadog.com/api/v1/events" \
        -H "Content-Type: application/json" \
        -H "DD-API-KEY: ${{ secrets.DATADOG_API_KEY }}" \
        -d '{
          "title": "Production Deployment",
          "text": "Deployed version ${{ github.sha }} to production",
          "tags": ["deployment", "production"]
        }'
```

---

## Best Practices

### Git Best Practices

#### Commit Guidelines

Commit frequently with clear, meaningful messages. Check your status often with git status to avoid surprises. Stage only what you intend to commit.

**Good Commit Messages:**
```bash
# Format: type(scope): description

feat(auth): add user authentication system
fix(api): resolve memory leak in user service
docs(readme): update installation instructions
refactor(utils): simplify date formatting function
test(auth): add unit tests for login validation
```

**Commit Message Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Build process or auxiliary tool changes

#### Branching Strategy

```mermaid
gitgraph
    commit id: "Initial"
    
    branch develop
    checkout develop
    commit id: "Setup dev"
    
    branch feature/user-auth
    checkout feature/user-auth
    commit id: "Add login"
    commit id: "Add logout"
    commit id: "Add validation"
    
    checkout develop
    merge feature/user-auth
    commit id: "Merge auth feature"
    
    branch release/v1.0
    checkout release/v1.0
    commit id: "Version bump"
    commit id: "Fix minor bugs"
    
    checkout main
    merge release/v1.0
    commit id: "Release v1.0"
    tag: "v1.0.0"
    
    checkout develop
    merge release/v1.0
```

**Branch Naming Conventions:**
- `feature/feature-name`: New features
- `bugfix/issue-description`: Bug fixes
- `hotfix/critical-issue`: Emergency fixes
- `release/version-number`: Release preparation
- `chore/task-description`: Maintenance tasks

### CI/CD Best Practices

#### Pipeline Design

CI/CD best practices include automation as the backbone of CI/CD, using reusable workflows to avoid duplication, securing secrets properly, and monitoring workflows regularly.

**Key Principles:**

1. **Automate Everything**
```yaml
# Automate testing, building, and deployment
on: [push, pull_request]
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - run: npm ci
    - run: npm run lint
    - run: npm test
    - run: npm run build
```

2. **Fail Fast**
```yaml
# Stop pipeline on first failure
jobs:
  test:
    steps:
    - name: Run tests
      run: npm test
      continue-on-error: false  # Default behavior
```

3. **Use Reusable Workflows**
```yaml
# .github/workflows/reusable-test.yml
name: Reusable Test Workflow
on:
  workflow_call:
    inputs:
      node-version:
        required: true
        type: string
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
    - run: npm ci
    - run: npm test

# .github/workflows/main.yml
name: Main CI
on: [push]
jobs:
  test-node-16:
    uses: ./.github/workflows/reusable-test.yml
    with:
      node-version: '16'
  test-node-18:
    uses: ./.github/workflows/reusable-test.yml
    with:
      node-version: '18'
```

#### Security Best Practices

**1. Secure Secrets Management**
```yaml
jobs:
  deploy:
    steps:
    - name: Deploy
      env:
        # Use secrets, never hardcode
        API_KEY: ${{ secrets.API_KEY }}
        DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
      run: deploy.sh
```

**2. Principle of Least Privilege**
```yaml
permissions:
  contents: read      # Only read repository contents
  deployments: write  # Only write to deployments
  # Don't grant unnecessary permissions
```

**3. Use Trusted Actions**
```yaml
steps:
# Pin to specific versions, not @main
- uses: actions/checkout@v4.1.1
- uses: actions/setup-node@v4.0.0
# Verify action publishers
```

#### Performance Optimization

**1. Caching Dependencies**
```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: '18'
    cache: 'npm'  # Automatic caching
    
- name: Cache custom directories
  uses: actions/cache@v3
  with:
    path: |
      ~/.cache
      node_modules
    key: ${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
```

**2. Parallel Jobs**
```yaml
jobs:
  test:
    strategy:
      matrix:
        test-group: [unit, integration, e2e]
    runs-on: ubuntu-latest
    steps:
    - run: npm run test:${{ matrix.test-group }}
```

**3. Conditional Execution**
```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'  # Only on main branch
    steps:
    - name: Deploy frontend
      if: contains(github.event.head_commit.modified, 'frontend/')
      run: deploy-frontend.sh
```

### Monitoring and Observability

#### Pipeline Monitoring

```yaml
jobs:
  notify-failure:
    runs-on: ubuntu-latest
    needs: [build, test, deploy]
    if: failure()
    steps:
    - name: Notify team of failure
      uses: 8398a7/action-slack@v3
      with:
        status: failure
        text: 'Pipeline failed for commit ${{ github.sha }}'
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

#### Application Monitoring

```yaml
post-deploy:
  steps:
  - name: Health check
    run: |
      for i in {1..5}; do
        if curl -f https://myapp.com/health; then
          echo "Health check passed"
          exit 0
        fi
        echo "Attempt $i failed, retrying..."
        sleep 10
      done
      exit 1
```

---

## Troubleshooting Guide

### Common Git Issues

#### 1. Merge Conflicts

**Problem:** Git cannot automatically merge changes
```bash
Auto-merging src/app.js
CONFLICT (content): Merge conflict in src/app.js
Automatic merge failed; fix conflicts and then commit the result.
```

**Solution:**
```bash
# 1. Open conflicted files and resolve conflicts
# Look for conflict markers: <<<<<<<, =======, >>>>>>>

# 2. Mark conflicts as resolved
git add src/app.js

# 3. Complete the merge
git commit -m "Resolve merge conflict in app.js"
```

#### 2. Accidental Commits

**Problem:** Committed sensitive data or wrong files

**Solutions:**
```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Undo last commit and discard changes
git reset --hard HEAD~1

# Remove file from last commit
git reset HEAD~1 <file>
git add .
git commit -m "Corrected commit"

# Remove sensitive data from history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch secrets.txt' \
  --prune-empty --tag-name-filter cat -- --all
```

#### 3. Branch Issues

**Problem:** Working on wrong branch

**Solution:**
```bash
# Save current work
git stash

# Switch to correct branch
git checkout correct-branch

# Apply saved work
git stash pop

# Or move commits to correct branch
git cherry-pick <commit-hash>
```

### Common CI/CD Issues

#### 1. Failed Builds

**Problem:** Dependencies fail to install

**Error Example:**
```
npm ERR! peer dep missing: react@>=16.8.0
```

**Solutions:**
```yaml
# Fix: Specify exact versions
- name: Install dependencies
  run: npm ci  # Use ci instead of install for reproducible builds

# Or: Clear cache and reinstall
- name: Clear npm cache
  run: npm cache clean --force
```

#### 2. Test Failures

**Problem:** Tests pass locally but fail in CI

**Common Causes & Solutions:**

```yaml
# Environment differences
- name: Set environment variables
  env:
    NODE_ENV: test
    TZ: UTC  # Set timezone
    
# Missing services
services:
  redis:
    image: redis:6
  postgres:
    image: postgres:13
    env:
      POSTGRES_PASSWORD: test
      
# File permissions (Linux/Windows differences)
- name: Fix permissions
  run: chmod +x ./scripts/test.sh
```

#### 3. Deployment Failures

**Problem:** Deployment succeeds but application doesn't work

**Debug Steps:**
```yaml
- name: Debug deployment
  run: |
    # Check application logs
    docker logs myapp
    
    # Verify environment variables
    env | grep -E '^(NODE_ENV|DATABASE_URL)'
    
    # Test endpoints
    curl -v https://myapp.com/health
    
    # Check disk space
    df -h
```

#### 4. Permission Issues

**Problem:** GitHub Actions lacks permissions

**Error:** `Permission denied`

**Solutions:**
```yaml
# Add necessary permissions
permissions:
  contents: read
  packages: write
  deployments: write
  
# Or for specific jobs
jobs:
  deploy:
    permissions:
      deployments: write
    steps:
    - name: Deploy
      run: deploy.sh
```

### Debugging Workflows

#### Enable Debug Logging

```yaml
# Add to workflow
env:
  ACTIONS_STEP_DEBUG: true
  ACTIONS_RUNNER_DEBUG: true
```

#### Debug Steps

```yaml
- name: Debug environment
  run: |
    echo "GitHub Context:"
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
    echo "Actor: ${{ github.actor }}"
    
    echo "Environment:"
    env | sort
    
    echo "Working Directory:"
    pwd
    ls -la
```

#### Test Workflows Locally

Use tools like [act](https://github.com/nektos/act) to test GitHub Actions locally:

```bash
# Install act
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Run workflow locally
act push

# Run specific job
act -j test

# Use custom environment
act -s GITHUB_TOKEN=your_token
```

---

## Additional Resources

### Learning Materials

#### Official Documentation
- [Git Documentation](https://git-scm.com/doc) - Complete Git reference
- [GitHub Actions Documentation](https://docs.github.com/en/actions) - Official GitHub Actions guide
- [GitHub Skills](https://skills.github.com/) - Interactive learning courses

#### Recommended Books
- **"Pro Git"** by Scott Chacon and Ben Straub - Comprehensive Git guide
- **"Continuous Delivery"** by Jez Humble and David Farley - CI/CD principles
- **"GitHub Actions in Action"** by Michael Kaufmann - Practical GitHub Actions

#### Online Courses
- [DataCamp Git Courses](https://www.datacamp.com/courses/introduction-to-git) - Interactive Git learning
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) - Visual Git guides
- [GitHub Learning Lab](https://lab.github.com/) - Hands-on GitHub practice

### Tools and Extensions

#### Git GUIs
- **GitHub Desktop** - Official GitHub GUI client
- **SourceTree** - Free Git GUI by Atlassian  
- **GitKraken** - Cross-platform Git GUI with advanced features
- **VS Code Git Integration** - Built-in Git support in VS Code

#### GitHub Actions Marketplace
- [Actions Marketplace](https://github.com/marketplace?type=actions) - 13,000+ pre-built actions
- **Popular Actions:**
  - `actions/checkout@v4` - Checkout repository code
  - `actions/setup-node@v4` - Setup Node.js environment
  - `docker/build-push-action@v4` - Build and push Docker images
  - `codecov/codecov-action@v3` - Upload code coverage

#### CLI Tools
```bash
# GitHub CLI
gh repo create myproject
gh pr create --title "Add new feature"
gh workflow run ci.yml

# Git aliases for productivity
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

### Cheat Sheets

#### Git Quick Reference

| Command | Description |
|---------|-------------|
| `git status` | Check repository status |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit with message |
| `git push origin main` | Push to remote |
| `git pull origin main` | Pull from remote |
| `git checkout -b feature` | Create and switch branch |
| `git merge feature` | Merge branch |
| `git log --oneline` | View commit history |
| `git reset HEAD~1` | Undo last commit |
| `git stash` | Save changes temporarily |

#### GitHub Actions Syntax

```yaml
# Basic workflow structure
name: Workflow Name
on: [events]
env:
  GLOBAL_VAR: value
jobs:
  job-name:
    runs-on: runner-type
    env:
      JOB_VAR: value
    steps:
    - name: Step Name
      uses: action@version
      with:
        parameter: value
      env:
        STEP_VAR: value
    - run: command
```

### Community and Support

#### Getting Help
- **GitHub Community Discussions** - Ask questions and share knowledge
- **Stack Overflow** - Search for `git` and `github-actions` tags
- **Discord/Slack Communities** - Real-time help from developers
- **Local Meetups** - Find Git and DevOps groups in your area

#### Contributing to Open Source
1. **Find projects** using GitHub's "Good First Issue" label
2. **Fork repositories** and create feature branches  
3. **Submit pull requests** with clear descriptions
4. **Participate in discussions** and code reviews

---

## Summary

This guide covered the essential concepts and practical implementation of Git, GitHub, and CI/CD:

### Key Takeaways

1. **Git is Essential** - Version control is fundamental for any development project
2. **GitHub Enhances Collaboration** - Remote repositories and pull requests streamline teamwork  
3. **CI/CD Improves Quality** - Automated testing and deployment reduce errors and increase efficiency
4. **GitHub Actions Simplifies Automation** - Native CI/CD integration makes setup straightforward
5. **Best Practices Matter** - Following conventions and security practices ensures long-term success

### Next Steps

1. **Practice with a real project** - Apply these concepts to your current work
2. **Set up your first GitHub Actions workflow** - Start with a simple test automation
3. **Explore advanced features** - Matrix builds, environments, and custom actions
4. **Share knowledge** - Teach these concepts to your team members
5. **Stay updated** - Follow GitHub's roadmap and new features

### Team Implementation Plan

1. **Week 1:** Git fundamentals training and repository setup
2. **Week 2:** GitHub workflow implementation and pull request process
3. **Week 3:** Basic CI/CD pipeline setup with GitHub Actions
4. **Week 4:** Advanced features and production deployment strategies

Remember: **Start small, iterate often, and gradually add complexity as your team becomes more comfortable with these tools and processes.**
