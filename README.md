[![main](https://github.com/matthewbrown77/CommitBot/actions/workflows/main.yml/badge.svg)](https://github.com/matthewbrown77/CommitBot/actions/workflows/main.yml)

# CommitBot
CommitBot is a system to hack your Github contributions graph and look way more consistently productive than you actually are. CommitBot will automatically create a variable numbers of commits in a private target repository each day. That way, you can boost your Github contribution graph without actually having to do any real work!

<p align="center">
  <img src="./img/contributions.png" alt="Github Contributions graph" width="738">
</p>

# Development
* Clone this repository on your computer.
* Create a `.env` file in the root directory containing your Github API token.
* Install the python dependencies with `pip install -r requirements.txt`.
* Run `python scripts/main.py` in the root directory.
* Run `python scripts/cleanup_repo.py` to delete the repository created by CommitBot.

# Usage
Interested in using CommitBot to boost your Github contribution graph? Simply fork this repository and configure a repository secret named `TOKEN` containing your personal Github API token.

Built for [HackGT 8](https://hack.gt) :heart