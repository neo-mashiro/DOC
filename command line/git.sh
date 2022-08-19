##  ------------------------------------------------------------------------------
##  0. Concepts
##  ------------------------------------------------------------------------------

# HEAD

  `HEAD` is a reference to "the most recent commit", when you switch to another branch, `HEAD` switches as well. No matter how many branches we have, there is always only one `HEAD` cursor per repository. `HEAD~1` is the commit before `HEAD`, while `HEAD~2` refers to the commit before `HEAD~1`, and so on.

# Git Objects

  Internally, Git uses objects to store four types of things. A typical Git user may only interact with commit objects and tags, letting Git worry about the details related to trees and blobs.

  1. A commit object is a simple text file that contains information such as the commit user information, commit message, a reference to the parent of the commit, and a reference to the root tree of the project. That information is all that Git needs to rebuild the full contents of a commit.
  2. An annotated tag is a reference to a specific commit.
  3. A tree is an object that contains a list of the filenames and directories inside of a directory.
  4. A blob is an object that stores the content of a file that is being managed by Git.

# Git ID

  The name of a Git object, a 40-character hexadecimal string, also known as object ID, SHA-1, hash and checksum.
  Git ID is a SHA-1 value, which is unique for a given piece of content (statistically speaking).

  git hash-object <file>  # create a SHA-1 for any content

# Git workflows

  1. Centralized Workflow (Manulife)
  2. Feature Branch Workflow (best for personal repositories)  # this is the one I use for my own account
  3. Gitflow Workflow (best for a large software company)
  4. Forking Workflow (most popular for open-source project collaboration)  # the one I use for open-source contribution

  (https://www.atlassian.com/git/tutorials/comparing-workflows)


##  ----------------------------------------------------------------------------
##  1. Getting started
##  ----------------------------------------------------------------------------

git --version  # check installation

git [command] [--flags] [arguments]  # Git syntax

git help [command]  # show the full help for a command
git help init       # show the full help for init
git help            # show the overall git help

git <command> -h    # concise help
git init -h


##  ----------------------------------------------------------------------------
##  2. Setup configuration
##  ----------------------------------------------------------------------------

git config [--local|--global|--system] <key> [<value>]

There are 3 levels of configuration. The `--system` flag applies to every repository for all users on your computer, the `--global` flag applies to every repository that you use on your computer, no flag or `--local` applies only to the current repository (highest precedence). Each level overrides the one above it, so local settings (per-project) take precedence over global settings (per-user), which in turn take precedence over system settings (for all users on the computer).

# global level
git config --global user.name neo-mashiro
git config --global user.email neo-mashiro@hotmail.com
git config --global core.editor nano
git config --global core.editor atom

# local level
git config user.name neo-mashiro
git config user.email neo-mashiro@hotmail.com


##  ----------------------------------------------------------------------------
##  3. Check configuration
##  ----------------------------------------------------------------------------

# show default settings for each level
git config --list --system
git config --list --global
git config --list --local

# git config <key>
git config user.name
git config user.email
git config core.editor

# check configuration file
ls .git
cat .git/config
cat .git/FETCH_HEAD


##  ----------------------------------------------------------------------------
##  4. Create a local repository, stage files and commit
##  ----------------------------------------------------------------------------

git init        # make . a Git repo
git init <dir>  # make <dir> a Git repo

git status

git clean -n    # show a list of untracked files in the repository
git clean -f    # !delete untracked files

git add <file/dir>  # add file/dir (tracked or untracked) to the staging area
git add -A          # stage all files

git commit -m "commit message"  # commit with just 1 line of message
git commit                      # launches core.editor to write long commit messages

In some cases, we may want to amend the current commit, unstage a file, or even revert a file to a previous state.

# amend the current commit, which creates a new SHA-1 hash value
git commit --amend
git commit --amend -m "change the commit message"

# undo the most recent commit
git reset --soft HEAD~

# reset the status of a file/dir (status = staged/unstaged/committed)
git reset HEAD <file>   # unstage a staged file
git reset HEAD <dir>    # unstage all staged files in the directory
git rm --cached <file>  # unstage a file

# revert an unstaged file/dir (staged files cannot be reverted, must unstage first)
git checkout -- <file>      # revert an unstage file to HEAD revision
git checkout -- <dir>       # revert all unstage files in dir to HEAD revision
git checkout 2242bd <file>  # revert to a specific revision (first find SHA-1 using git log <file>)


##  ----------------------------------------------------------------------------
##  5. View commit details and history
##  ----------------------------------------------------------------------------

git log         # press the space bar to go down a page or 'q' to quit
git log <file>  # show change logs of the file
git log <dir>   # show when files were added or deleted in the directory

git annotate <file>   # details of changes on a file

git log --oneline     # one line for each commit, from the most recent to the least recent
git log --oneline -3  # -3 limits the log to the most recent 3 commits

git log --oneline --graph        # a commit graph is much more straightforward than text logs
git log --oneline --graph --all  # --all option will show all local and remote tracking branches

git log origin --oneline  # show commit history of only remote branches (on Github/Bitbucket)

A typical commit graph looks like this:
--------------------------------------------------------------------------------
* f8cbf90 (HEAD -> master) Merge branch 'feature1'  # 1st line: the most recent commit (the current commit)
|\
| * 4684dcf 2nd commit on feature1
| * 1cd70bb 1st commit on feature1
|/
* c126179 initial commit                            # last line: the least recent commit (initial commit)
--------------------------------------------------------------------------------

To see how a file has been changed between commits, we can use `git diff`.
Unstaged files are not tracked, so `git diff` only works with staged files.

git diff                   # diff all files with HEAD
git diff <file>            # diff the file with HEAD
git diff <dir>             # diff all files in the dir with HEAD
git diff HEAD~2            # diff with HEAD~2
git diff -r def456 <file>  # -r: compare to a particular revision
git diff abc123..def456    # diff between 2 commit revisions
git diff HEAD~1..HEAD~3
git diff HEAD..HEAD~1
git diff master..featureX  # diff all files between 2 branches


##  ----------------------------------------------------------------------------
##  6. Add a remote repository
##  ----------------------------------------------------------------------------

A remote repository is often a "bare" repository. By convention, remote repository names end with `.git`.
First, we need to manually create a remote repository on Github, Bitbucket or other hosting providers.

https://github.com/user_name/repo_name.git
https://bitbucket.org/user_name/repo_name.git

When it comes to pushing our work to the remote, there are two scenarios here.
1. If we already have a local repository with work to push, we only need to associate it with a remote.
2. Otherwise, we must first clone a repository from remote to local, this way, local and remote are automatically associated with each other, and Git will name this remote as `origin`. Then we make some changes to the local, and finally push our work to the remote.

# scenario 1
git remote add <remote-name> <url>  # add a remote url to the local repo, and give this remote a name
git remote add origin https://github.com/neo-mashiro/LeetCode.git  # the default name of the remote is origin

# scenario 2
git clone https://github.com/user_name/repo_name.git  # make a local copy in the current dir
git clone file:///some_folder/repo-name               # clone from an existing local repo
cd repo_name

Once the connection between local and remote has been established, we can check information about the remote.
It is worth mentioning that a remote can have several different URLs for different purposes.

git remote                 # show the remote for the local repo, if no remotes, nothing happens
git remote -v              # --verbose
git remote get-url origin  # show the url of remote 'origin'
git remote rm remote-name  # remove a remote, disconnect it from local, this is barely used


##  ----------------------------------------------------------------------------
##  7. Push local commits to the remote repository
##  ----------------------------------------------------------------------------

We must ensure that the local repo is up-to-date with the remote before pushing, otherwise the push would fail.

git push [-u] [<remote-name>] [<branch>]  # the -u option tells Git to track this upstream branch in the remote

git push -u origin master  # for the first time push, specify -u
git push origin master
git push


##  ----------------------------------------------------------------------------
##  8. Directed Acyclic Graph (DAG), Commit Graphs
##  ----------------------------------------------------------------------------

Git models the relationship of commits with a DAG.
--------------------------------------------------------------------------------
* f8cbf90 (HEAD -> master) Merge branch 'feature1'
|\
| * 4684dcf 2nd commit on feature1
| * 1cd70bb 1st commit on feature1
|/
* c126179 initial commit
--------------------------------------------------------------------------------


##  ----------------------------------------------------------------------------
##  9. Tags
##  ----------------------------------------------------------------------------

A tag is an user-defined reference to a specific commit. Tags can be used instead of branch labels or Git IDs in Git commands.
By convention, the tag is named 'v#.#' such as 'v1.0' or 'v1.3', depending on if it is a major release or a hot fix.

git push         # git push does not automatically transfer local tags to the remote
git push --tags  # to transfer tags, we must add the `--tags` option

git tag              # view all tags
git tag v1.0         # tag the current commit as v1.0
git tag v0.1 HEAD~1  # tag the previous commit as v0.1

# several ways to show details for a given commit
git show v1.0    # by tag
git show 17d5    # by SHA-1 hash value (shortened, 4 digits)
git show 17d5ed  # by SHA-1 hash value (shortened, 6 digits)
git show HEAD    # by HEAD
git show master  # show all commits of a branch

git tag -a -m <msg> <tagname> [<commit>]  # tag a commit (defaults to HEAD)
git tag -a -m "tag the current commit which fixed a small bug" v0.1
git tag -a -m "tag the previous commit which is the initial release" v0.0 HEAD~1

git tag -d v0.1  # remove a tag

git push origin v0.1    # push a single tag to remote
git push origin --tags  # push all tags to remote


##  ----------------------------------------------------------------------------
##  10. Branches
##  ----------------------------------------------------------------------------

When we create a new branch, the contents of the new branch are initially identical to the contents of the current active branch. If we want to switch to another branch, the current branch must be clean. If the current branch has unsaved work, checkout will fail, we must commit first. When we switch to a new branch, `HEAD` switches as well. Commits made on different branches are mutually independent, they are only visible to their own branch. Keep in mind that branches are parallel.

git branch          # show all local branches, where * points to the current active branch
git branch --all    # show all local and remote tracking branches

git branch <name>   # create a new branch
git branch stream   # create a branch called 'stream'
git branch -d <br>  # delete a branch <br>, error if <br> is not merged to master
git branch -D <br>  # delete <br> even if it's not empty, which means to give up one's work on that branch

git checkout <name>  # switch to a branch
git checkout master
git checkout stream
git checkout -b stream  # create a new branch and switch to it, in one command

git reflog  # show a list of the recent commits that HEAD pointed to


##  ----------------------------------------------------------------------------
##  11. Fast-forward merge
##  ----------------------------------------------------------------------------

A fast-forward merge is possible if no other commits have been made to the master branch since branching.
A fast-forward merge is only a merge, but not a commit. After the merge, the commit history is linear.

A topic branch refers to the branch that we merged from, or, the branch that makes a hot fix.
After the merge, the master branch has all the information from the topic branch.
After the merge, the topic branch is still there, usually we should remove it (unless it is the remote tracking branch 'origin/master').
In case we want to keep that topic branch, there is nothing we need to do since it is clean and up-to-date.

git checkout master     # switch to master branch from feature1 branch (feature1 is clean), now HEAD points to master
git merge feature1      # attempt a fast-forward merge
git branch -d feature1  # remove feature1 branch if necessary

In some cases, we might be required to make a merge commit even if it is fast-forwardable, to keep track of every pull request.

git checkout master
git merge --no-ff stream  # no fast-forward
git branch -d stream

So which one works for you? It depends on your personal taste and the version control policy of your team.
By default, Github will perform the merge with the `--no-ff` option, read more at (https://ariya.io/2013/09/fast-forward-git-merge)


##  ----------------------------------------------------------------------------
##  12. Merge commit
##  ----------------------------------------------------------------------------

A merge commit occurs when 2 branches modify the same hunk in the same file, it combines the commits at the tips of the merged branches.
A merge commit is not fast-forwardable because the master branch has been updated since branching.
A merge commit is not only a merge, but also a new commit, because we are combining two different commit objects.
In this case, `git merge` opens the core editor showing a default merge message, which is the commit message for the merge commit.
After the merge commit, the commit history becomes non-linear.

git checkout master     # switch to master branch from feature1 branch (feature1 is clean), now HEAD points to master
git merge feature1      # if no conflict detected, git opens the core editor for you to edit the merge commit message
git branch -d feature1  # remove if necessary, otherwise push to update it

If both branches (master and feature1) have modified the same file, then there could be a merge conflict, otherwise there is no conflict.
We can only say "could be" because Git has the ability to automatically merge changes to different parts (hunks) of a file.
If both branches modified the same file, but each branch modified a different hunk, there is no conflict.
When attempting a merge, files with conflicts are modified by Git and placed in the working tree.

git checkout master     # now HEAD points to master
git merge feature1      # a conflict has been detected, both branches modified fileA.txt
git status              # now check where the conflict is in fileA.txt
                        # now fileA.txt has been modified by Git, which shows this content:
                        -----------------------------------------------------------------------------
                        initial commit        # unconflicted hunk
                        <<<<<<< HEAD          # <<<<<<< start of the conflicted hunks
                        added feature 2       # changes made on master branch (HEAD points to master)
                        =======               # ======= a separator line
                        added feature 1       # changes made on feature1 branch
                        >>>>>>> feature1      # >>>>>>> end of the conflicted hunks
                        -----------------------------------------------------------------------------
............            # now open fileA.txt with gedit/atom/vim, delete the content above, then fix it
cat fileA.txt           # double check if fileA.txt has been correctly fixed
git add fileA.txt       # stage the file to commit
git commit              # now git opens the core editor for you to edit the merge commit message
git log --oneline --graph --all  # after the merge, check the commit history
git branch -d feature1           # remove if necessary, otherwise push to update it

A merge commit is created only on the branch that we checked out (merged into), but not on the branch that we merged from.
After the merge commit, the checked out branch has all the information from the topic branch, but the topic branch is outdated.
If the topic branch is just another feature branch, we may want to remove it after the merge commit, or keep it as part of the history.
If we need to do more work later on that topic branch, we should push to it, or switch back to it and pull (either way is a fast-forward merge).
If the topic branch is the remote tracking branch 'origin/master', we should always push to it (fast-forwardable).

It is recommended to make small, frequent merges which are quite easy.
It is not recommended to make a giant merge after a long time, which may include many conflicts and many branches.
If a merge involves more than 3 branches and sub-branches, the merge can be very complex and error-prone.

git merge <into_branch> <from_branch>  # we can condense 'checkout' and 'merge' into a one-line command
git merge feature1 master              # merge master into feature1
git merge master feature1              # merge feature1 into master


##  ----------------------------------------------------------------------------
##  13. Network commands: fetch, pull, push
##  ----------------------------------------------------------------------------

git fetch [<repository>]  # retrieve updates from another repository (defaults to 'origin')
git fetch                 # fetch does not merge (even if it's fast-forwardable), so HEAD cursor will not update
git status                # after fetch, local branch is behind 'origin/master' by 1 commit
git merge FETCH_HEAD      # to clean up, merge by hand

git pull [<repository>] [<branch>]  # pull = fetch + merge, the tracking branch is merged into the local branch
git pull origin master              # make sure local is clean before pull, to make life easier

# merging options
git pull --ff       # (default) fast-forward if possible, otherwise perform a merge commit
git pull --no-ff    # always include a merge commit
git pull --ff-only  # (safe) only accepts fast-forward merges, otherwise cancel the pull

After a merge commit has been created on the local branch, the remote is outdated.
The remote does not know about this merge commit, so we must git push to let it know.
In this case, since a merge has already been made, the push will always be fast-forwardable, no conflicts.

git push [-u] [<remote-name>] [<branch>]  # the -u option tells Git to track this upstream branch in the remote
git push -u origin master
git push origin master

In order to make life easier, it is suggested to fetch or pull before push, and make local clean before fetch or pull.


##  ----------------------------------------------------------------------------
##  14. Rebase to rewrite the commit history
##  ----------------------------------------------------------------------------

https://git-scm.com/docs/git-rebase
https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing

Rebase reapplies commits of the feature branch to the tip of the master branch.
Since the commit chain has been changed, each of the reapplied commits is a new commit and has a new commit ID.
Reapplying commits is a form of merge, so rebase is susceptible to merge conflicts (both branches modified the same hunk of the same file).

git checkout <branch>  # switch to <branch>
git rebase <upstream>  # change its parent to <upstream>
git rebase <upstream> <branch>  # condense into a one-line command

git checkout feature1  # HEAD points to feature1
git rebase master      # rebase feature1 based on master
git status             # check if there's a rebase conflict, fix it
cat fileA.txt
git add fileA.txt      # stage the file with conflicts
git rebase --continue  # continue the rebase
git status             # now working tree is clean
git log --oneline --graph --all  # check the commit history after rebase

git rebase --abort     # abort the rebase, get back to the pre-rebase state

git rebase -i <base>   # interactive rebase, which can squash, ammend, delete each commit history, read docs for details

# why should we use rebase?
Rebase keeps the working tree clean and makes it easier to track commit history.
Most open-source projects use the forking workflow where developers first fork the upstream repo and then work on it.
In this case, rebase is a common way to integrate upstream changes into our forked local repository, to keep it updated with the upstream.
In contrast, pull in upstream changes with Git merge results in a superfluous merge commit every time.
The upstream repo only deals with pull requests, and developers do not have direct write access on the upstream.
Rebase facilitates pull requests, facilitates a later fast-forward merge of our feature branch back into the master branch.

# !caution
1. Never rebase commits once they have been pushed to a public repository.
2. Never rebase the master branch based on a topic branch, we should only use merge to update master.
3. Rebase is dangerous, other developers on the team may lose their code if you use rebase with the -f option.


##  ----------------------------------------------------------------------------
##  15. Squash merge
##  ----------------------------------------------------------------------------

A squash merge combines all commits on the topic branch and integrates them into one commit.
A squash merge is very much like a merge commit, but it rewrites the commit history.
A squash merge does not move `HEAD`, so we need an additional "git commit" command right after squash.

After a squash merge, the topic branch will be empty because we have squashed all the information into the last merge commit.
After we delete the feature1 branch, original commits on that branch no longer exist and will eventually be garbage collected.
When we merge a topic branch into master, if the commit history of the topic branch is unimportant, we should use squash merge.

git checkout master
git merge --squash feature1      # squash all commits from feature1 into 1 single commit, and merge it into master
git status                       # if there's a merge conflict, fix it
git commit -m "squash merge"     # after squash, fix detached HEAD cursor
git status                       # now working tree is clean
git log --oneline --graph --all  # check the commit history after squash merge
git branch -D feature1           # remove feature1 which is empty

git gc  # garbage collect


##  ----------------------------------------------------------------------------
##  16. Pull requests
##  ----------------------------------------------------------------------------

git checkout -b "featureX"               # create a feature branch
touch fileA.txt                          # work on the feature branch
git add fileA.txt
git commit -m "added featureX"
git push --set-upstream origin featureX  # push the branch to the remote
.........                                # create a pull request on Github/Bitbucket web interface, submit it
.........                                # review the pull request, approve/decline/edit it
.........                                # if approved, click merge to begin the process of merging the branch
git push -d origin featureX              # delete the featureX branch on the remote

If our remote repository is a forked copy of the original upstream, we are using the forking workflow.
When we create a pull request on the forked remote, Git recognizes this automatically and creates that pull request on the real upstream.


##  ----------------------------------------------------------------------------
##  17. Github workflow
##  ----------------------------------------------------------------------------
There are two main types of development models.
1. fork -> develop -> open pull request -> merge to upstream. This model is popular with open source projects.
2. collaborators are granted push access to a single shared repository and topic branches are created when changes need to be made. This model is more prevalent with small teams and organizations collaborating on private projects.

In the fork and pull model, from time to time we may need to sync our forked repo with the upstream repo.

# option 1: merge (not recommended), this will create an extra commit
git remote -v  # first make sure you have added a remote that points to the upstream repository
git remote add upstream https://github.com/other_user/original_repo.git

git fetch upstream
git checkout master        # local master branch
git merge upstream/master  # upstream master branch
git push origin master     # forked repo master branch, add --follow-tags if you have tags to push

# option 2: rebase (recommended), this will rewrite the history of your master branch, but further pull requests are clean
git fetch upstream
git checkout master
git rebase upstream/master
git push -f origin master  # force the push to your own forked repository on GitHub

if the upstream repository is deleted, one of the existing public forks is chosen to be the new parent repository. All other repositories are forked off of this new parent and subsequent pull requests go to this new parent.


##  -------------------------------------------------------------------------------------------------
##  * Shrink the Git repo by completely removing large files while maintaining all the commit history
##  -------------------------------------------------------------------------------------------------

https://github.com/rtyley/bfg-repo-cleaner


##  -------------------------------------------------------------------------------------------------
##  * Update in Git 2.23
##  -------------------------------------------------------------------------------------------------
To split and clarify the two different uses of git checkout, we now have 2 new commands.

git switch <branchname>  # change branches, same as git checkout <branchname>
git restore <file>       # reset files to certain revisions


##  -------------------------------------------------------------------------------------------------
##  * Example - Working with a small team that shares a repository
##  -------------------------------------------------------------------------------------------------
The scenario is that a small group of people are working on a shared repository. Each member develops on his/her own feature branch, then make a pull request to merge onto master.
Usually, the team wants to preserve the Git history for review purposes, the remote branches are never removed so there can be thousands of branches.
In this case, it's better to use visualization tools like gitk to assist your workflow, and frequently rebase your feature branch onto master.
The Git history will no longer be linear, but we should use squash merge as much as possible to clean up our pull request, and do local housekeeping.
Each time before we do the push, or we know there's a new release on the remote/master, we must pull on a regular basis to make sure our local master is up to date.
Keep in mind that we should never touch the master branch, development must be done on topic branches.
The remote master is only updated by merging pull requests on Github, the local master is only updated by pulling from remote master.

# make sure local master is up to date, check frequently
git switch master
git pull origin master
gitk --all  # don't just look at the active branch

# Case 1: if there's no new releases in the remote master branch, we can create a PR directly, but it's still good to check

git switch feature
git add file
git commit -m "add feature"
git push origin feature

# Case 2: while we work on our topic branch, the remote master has been updated (most common), must rebase before submit PR

git switch feature
git add file
git commit -m "add feature"
git commit -m "clean up format"

git switch master
git pull origin master
git switch feature
git rebase -i master
git push origin feature

# Case 3: similar to the prior case, but after we create the PR (and before it's merged), the remote master has new updates. In this case, we need to rebase again while the PR is waiting for approval, which will cause the topic branch to diverge from its remote ref, so a normal push will be rejected. Watch the gitk graph carefully, and then do a force push. The change will also be reflected in the Github pull request page.

git switch feature
git add file
git commit -m "add feature"
git push origin feature

git switch master
git pull origin master
git switch feature
git rebase master
git push -f origin feature  # since we have altered the history, we need to do a force push
