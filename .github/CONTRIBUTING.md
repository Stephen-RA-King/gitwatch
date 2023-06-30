Thank you for considering improving gitwatch, any contribution is most welcome!

# Requesting a new feature

If you would like to suggest a new feature, you can create a [feature request](https://github.com/Stephen-RA-King/gitwatch/issues/new?&template=feature_request.md).

# Reporting a bug

If you encountered an unexpected behavior, please [open a new issue](https://github.com/Stephen-RA-King/gitwatch/issues/new)
and describe the problem you have found.

An ideal bug report includes:

-   The Python version you are using.
-   The gitwatch version you are using (you can find it with `gitwatch --version`)
-   Your operating system name and version.
-   Your development environment and local setup (IDE, Terminal, project context, any relevant information that could be useful).
-   Some [minimal reproducible example](https://stackoverflow.com/help/mcve).

# Implementing changes

If you want to enhance gitwatch by implementing a changes, please [open a new issue](https://github.com/Stephen-RA-King/gitwatch/issues/new) first.

Then, implement the following workflow:

1.  Fork the [gitwatch](https://github.com/Stephen-RA-King/gitwatch) project from GitHub.

2.  Create a virtual environment with your favourite tool (virtualenv with virtualenv wrapper, venv etc)
    using one of the supported versions of Python: ![](https://img.shields.io/pypi/pyversions/gitwatch).

3.  Activate your virtual environment.

4.  Clone the repository locally:

        $ git clone git@github.com:Stephen-RA-King/gitwatch.git
        $ cd gitwatch

5.  Install gitwatch in development mode:

        $ pip install -e .

6.  Install pre-commit hooks that will check your commits:

        $ pre-commit install --install-hooks

7.  Create a new branch from `main`:

        $ git checkout main
        $ git branch fix_bug
        $ git checkout fix_bug

8.  Implement the modifications. During the process of development, honor [PEP 8](https://www.python.org/dev/peps/pep-0008/) as much as possible.

9.  Add unit tests and ensure all are passing:

        $ tox

10. Update the documentation.

11. If your development modifies gitwatch behavior, update the `CHANGELOG.md` file with your changes.

12. `add` and `commit` your changes, then `push` your local project:

        $ git add .
        $ git commit -m 'Add succinct explanation of what changed'
        $ git push origin fix_bug

13. If previous step failed due to the pre-commit hooks, fix reported errors and try again.

14. Finally, [open a pull request](Stephen-RA-King/gitwatch/compare) before getting it merged!
