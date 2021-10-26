import logging
import os
import random

from dotenv import load_dotenv
from github import Github, GithubException

from consts import CONST

load_dotenv()
g = Github(os.getenv('GITHUB_TOKEN'))
user = g.get_user()

if CONST.REPO_NAME not in [repo.name for repo in user.get_repos()]:
    logging.info('Repo not found, creating...')
    user.create_repo(CONST.REPO_NAME, private=True)
    
repo = user.get_repo(CONST.REPO_NAME)

for commits in range(random.randint(1, 20)):
    try:
        contents = repo.get_contents(CONST.FILE_NAME)
        commit = repo.delete_file(contents.path, "Remove test", contents.sha, branch=CONST.BRANCH_NAME)
        logging.info(commit)
    except GithubException as e:
        commit = repo.create_file(CONST.FILE_NAME, "Add test", "test", branch=CONST.BRANCH_NAME)
        logging.info(commit)
