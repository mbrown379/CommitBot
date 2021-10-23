import os

from dotenv import load_dotenv
from github import Github

from consts import CONST

load_dotenv()

g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_user().get_repo(CONST.REPO_NAME)
repo.delete()