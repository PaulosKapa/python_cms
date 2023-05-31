from github import Github
access_token = input("password: ")
g = Github(access_token)
repo_owner = 'ipermeleti'
repo_name = 'ipermeleti.github.io'
repo = g.get_user(repo_owner).get_repo(repo_name)
file_path = 'ipermeleti.github.io-main/sdfa.html'
commit_message = 'Commit message'

# Read the file content
with open(file_path, 'r') as file:
    file_content = file.read()

# Create or update the file
repo.create_file(file_path, commit_message, file_content, branch='main')
branch = repo.get_branch('main')
branch.edit(branch.commit.sha, force=True)
