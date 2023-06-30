# Core Library modules
import difflib
from pathlib import Path

# Third party modules
from git import Repo

root = Path("/")
REPO_DIR = root / "gitwatch" / "tryout"
col_width = 21


def print_message(message: str) -> None:
    message_length = len(message) + 20
    print(f"\n{'=' * message_length}")
    print(f"={' ' * 8} {message} {' ' * 8}=")
    print(f"{'=' * message_length}")


def repository_info(repo: Repo) -> None:
    message = "REPOSITORY INFORMATION"
    print_message(message)
    print(f"{'Description:':20} {repo.description}")
    print(f"{'Active Branch:':20} {repo.active_branch}")
    for remote in repo.remotes:
        print(f"{'Remote:':20} {remote}, URL: {remote.url}")
    print(f"{'Last commit:':20} {str(repo.head.commit.hexsha)}")


def commit_data(commit_no: int) -> None:
    message = f"COMMIT DATA FOR THE LAST {commit_no} COMMIT{'S'[:commit_no^1]}"
    print_message(message)
    commits = list(repo.iter_commits(f"{repo.active_branch}"))[:commit_no]
    for commit in commits:
        print(f"{'Commit SHA1:':20} {commit.hexsha}")
        print(f"{'Summary':20} {commit.summary}")
        print(f"{'Author:':20} {commit.author.name}")
        print(f"{'Author eMail:':20} {commit.author.email}")
        print(f"{'Authored Date:':20} {commit.authored_datetime}")
        print(f"{'Committer:':20} {commit.committer.name}")
        print(f"{'Committer eMail:':20} {commit.committer.email}")
        print(f"{'Committed Date:':20} {commit.committed_datetime}")
        print(str(f"count: {commit.count()}"))


def branches() -> None:
    message = "Branches"
    print_message(message)
    heads = repo.heads
    print(f"{'Branches:':20} {len(heads)}\n")
    for head in heads:
        print(f"{head.name}")


def tags() -> None:
    message = "Tags"
    print_message(message)
    tags = repo.tags
    print(f"{'Tags:':20} {len(tags)}\n")
    for tag in tags:
        print(f"{tag.name}")


def remote_sync_status() -> None:
    message = "MAIN AND ORIGIN/MAIN SYNC STATUS"
    print_message(message)
    o = repo.remotes.origin
    o.fetch()
    commits_behind = repo.iter_commits("main..origin/main")
    commits_ahead = repo.iter_commits("origin/main..main")
    count_ahead = sum(1 for _ in commits_ahead)
    count_behind = sum(1 for _ in commits_behind)
    if count_ahead != 0 and count_behind != 0:
        rec_action = "PULL then PUSH"
    elif count_ahead == 0 and count_behind != 0:
        rec_action = "PULL"
    elif count_ahead != 0 and count_behind == 0:
        rec_action = "PUSH"
    else:
        rec_action = "NONE"
    print("main compared to origin/main is:")
    print(f"{'Commits Ahead:':20} {count_ahead}")
    print(f"{'Commits Behind:':20} {count_behind}")
    print(f"{'Action Required:':20} {rec_action}")


def branch_sync_status() -> None:
    pass


def remote_file_diff() -> None:
    message = "FILE CONTENT DIFFS BETWEEN MAIN and ORIGIN/MAIN"
    print_message(message)
    commit_dev = repo.commit("main")
    commit_origin_dev = repo.commit("origin/main")
    diff_index = commit_origin_dev.diff(commit_dev)
    print(f"{'Total Files Modified:':20} {len(diff_index)}")

    for diff_item in diff_index.iter_change_type("M"):
        a_blob = diff_item.a_blob.data_stream.read().decode("utf-8")
        a_blob = a_blob.strip().splitlines()
        a_file = str(diff_item.a_rawpath)
        print(a_file)
        b_blob = diff_item.b_blob.data_stream.read().decode("utf-8")
        b_blob = b_blob.strip().splitlines()
        b_file = str(diff_item.b_rawpath)
        print(b_file)
        for line in difflib.unified_diff(
            a_blob, b_blob, fromfile=a_file, tofile=b_file, lineterm=""
        ):
            print(line)


def unstaged_files() -> None:
    message = "UNSTAGED FILES"
    print_message(message)
    print(f"{'Unstaged Files:':20} {len(repo.index.diff(None))}\n")
    for item in repo.index.diff(None):
        print(f"{'a_path:':20} {item.a_path}")
        print(f"{'a_mode:':20} {item.a_mode}")
        print(f"{'a_blob:':20} {item.a_blob}")
        print(f"{'b_path:':20} {item.b_path}")
        print(f"{'b_mode:':20} {item.b_mode}")
        print(f"{'b_blob:':20} {item.b_blob}")
        print(f"{'Change Type:':20} {item.change_type}")
        print(f"{'New File:':20} {item.new_file}")
        print(f"{'Copied File:':20} {item.copied_file}")
        print(f"{'Deleted File:':20} {item.deleted_file}")
        print(f"{'Renamed File:':20} {item.renamed_file}")
        print("-------------------------------\n")


def untracked_files() -> None:
    message = "UNTRACKED FILES"
    print_message(message)
    untracked_list = repo.untracked_files
    print(f"{'Untracked Files:':20} {len(untracked_list)}\n")
    for file in untracked_list:
        print(file)


if __name__ == "__main__":
    repo = Repo(REPO_DIR)
    if not repo.bare:
        print("Repo successfully loaded.")
        repository_info(repo)
        untracked_files()
        unstaged_files()
        branches()
        tags()
        commit_data(1)
        remote_sync_status()
        remote_file_diff()
    else:
        print(f"Could not load repository at {REPO_DIR} :")
