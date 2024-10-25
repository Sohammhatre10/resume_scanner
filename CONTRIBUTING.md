# Contributing to Resume Scanner

Thank you for your interest in contributing to the Resume Scanner project! We welcome all contributions—whether it’s reporting issues, improving documentation, fixing bugs, or adding new features. Please follow the guidelines below to ensure a smooth collaboration.

TL;DR

1. [Open an Issue](#reporting-issues)
2. [Fork the repository](#forking-the-repository)
3. [Making changes](#making-changes)
4. [Syncing your fork to avoid conflict](#avoid-conflicts-syncing-your-fork)
5. [Submit a pull request](#submitting-a-pull-request)
6. [Maintainers review](#reporting-issues)

## How to Contribute:

### Reporting Issues

If you find a bug or have suggestion for an enhancement, please [open an issue](https://github.com/Sohammhatre10/resume_scanner/issues) with the following information:

- A detailed description of the problem or idea.
- Steps to reproduce the issue (if applicable).
- Screenshots or logs that help illustrate the issue.

### Forking the Repository

1. Fork the repository to your own GitHub account.
2. Clone the forked repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/resume_scanner.git
   ```

3. Create a new branch for your contribution:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Making Changes

- Keep your changes focused and small to make it easier to review.
- Follow the project's coding style and best practices.
- Ensure that your code includes relevant comments and documentation.

### Branch Naming Conventions

- Use descriptive name for your branches. For example:
  - `feature/your-feature-name` for new features.
  - `fix/issue-description` for bug fix.

### Avoid Conflicts (Syncing your fork)

To avoid merge conflicts, it's important to keep your fork in sync with the original repository, as other pull requests (PRs) may be merged while you're working on your branch. Here’s how you can do that:

1. **Add an 'Upstream' Remote**

   Adding an upstream remote allows you to fetch changes from the original repository:

   ```bash
   git remote add upstream https://github.com/Sohammhatre10/resume_scanner.git
   ```

2. **Verify the Remote**

   You can verify that the upstream remote has been added by running:

   ```bash
   git remote -v
   ```

   You should see both your fork (origin) and the upstream remote listed.

3. **Sync with the Upstream Repository**
   To pull the latest changes from the original repository and merge them into your branch, run:

   ```bash
   git fetch upstream
   git merge upstream/main
   ```

   This will fetch any new changes from the main branch of the parent repository and merge them into your current branch.

4. **Resolve Conflicts**

   If there are any merge conflicts, Git will alert you, and you can resolve them manually by editing the conflicting files. Once resolved, commit the changes:

   ```bash
   git add .
   git commit -m "Resolved merge conflicts"
   ```

5. **Keep Your Fork Up to Date**

   It’s a good idea to regularly fetch changes from the upstream repository, especially before you start working on a new feature or submit a pull request. This ensures your fork is always up to date with the latest changes from the main project.

### Submitting a Pull Request

Once your changes are ready:

1. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Open a Pull Request from your branch to the `main` branch of the original repository.
3. In the pull request description, mention the issue your PR addresses (if applicable) and explain your changes in detail.

### Review Process

A project maintainer will review your pull request. The review process may include suggestions or requests for changes. Be patient, and feel free to ask questions if needed.

### Documentation Contributions

If you are contributing to the documentation (e.g., improving the `README.md` or adding new files), ensure your changes are:

- Clear and concise.
- Organized under relevant sections.
- Include code snippets or examples, if necessary.
