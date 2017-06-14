---
layout: post
title: "Git: An introduction!"
date: 2015-12-01
excerpt_separator: <!--more-->
---

OK. So you are an devops engineer and a religious devOps engineer should be practicsing and using Git. Not to mention the enormous benifits provided by git, its without doubt is the best SCM available there.
Git is different from the other SCM's available in market. This ariticle I will be explaining basic concepts of git and the practical and useful commands of git (with not sh*t!).


One of the most important job any SCM does it to give us ability to see what has changes in data/files over the period of time, and revert to any previous change when needed. Most of the SCM acheive this by maintaing a list of file based changes. Git, on the other hand does this differently and leverages snapshots.

<!--more-->


## How git differs from other VCS?

As aforesaid, git uses snapshot to store information about what has changed. Every commit in git results in picture of files during that time and git the creates a reference to this.

Things to keep in mind regarding git:

- Almost of the operations are local.
- To examplify to see a list of changes done of a file a month back, git does not goes to internet. Rather, it can refer to the local database it stores.
- There are not many things you *cannot* do if you are not online using git.

### Three stages of git:

1. Working directory : This is where you store your modified files.
2. Index (Stage) : The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit. It’s sometimes referred to as the “index”, but it’s also common to refer to it as the staging area. 
3. Committed (HEAD): This is where the snapshot are stored.

To relate with Git commands:

Working directory (You modify files here) --> git status will show these modified files.
Index : git add [-A|or file list ] will mark the files you have selected to be added to the next commit.
Commited(HEAD): git commit -m "some meaning full message": This will create a snapshot with details of what has changed in the files added in Index stage.

Alright, enough of theory, time to put git commands line in action:

- We will be using a repo named "repo1"
- It has a readme.md file in it.



