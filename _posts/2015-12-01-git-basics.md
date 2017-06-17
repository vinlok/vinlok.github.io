---
layout: post
title: "Git: An introduction!"
date: 2015-12-01
excerpt_separator: <!--more-->
---

OK. So you are an devops engineer and a religious devOps engineer should be practicsing and using Git. Not to mention the enormous benifits provided by git, its without doubt is the best SCM available there.
Git is different from the other SCM's available in market. This ariticle aims at basic concepts of git with highlight on practical and useful commands.

One of the most important job any SCM does it to give us ability to see what has changes in data/files over the period of time, and revert to any previous change when needed. Most of the SCM acheive this by maintaing a list of file based changes. Git, on the other hand does this differently and leverages snapshots.

<!--more-->

---
### How git differs from other VCS?

As aforesaid, git uses snapshot to store information about what has changed. Every commit in git results in picture of files during that time and git the creates a reference to this.

Things to keep in mind regarding git:

- Almost of the operations are local.
- To examplify to see a list of changes done of a file a month back, git does not goes to internet. Rather, it can refer to the local database it stores.
- There are not many things you *cannot* do if you are not online using git.

---
### Three stages of git:

1. Working directory : This is where you store your modified files.
2. Index (Stage) : The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit. It’s sometimes referred to as the “index”, but it’s also common to refer to it as the staging area. 
3. Committed (HEAD): This is where the snapshot are stored.

To relate with Git commands:

1. Working directory (You modify files here): git status will show these modified files.
2. Index : git add [-A or file list ] will mark the files you have selected to be added to the next commit.
3. Commited(HEAD): git commit -m "some meaning full message": This will create a snapshot with details of what has changed in the files added in Index stage.

Alright, enough of theory, time to put git commands line in action:

---
### Setting git variables:

First thing first, you should always setup git configuration variables. To name a few are user.name, user.email. The git variables are stored in config files and the order of precedence is as below (low to high)

1. /etc/gitconfig - For all users on a given system. Can be accessed with git config --system
2. ~/.gitconfig or ~/.config/git/config file: Specific to current user. Can be accessed with git config --global
3. config file in the Git directory (that is, .git/config): Specific to current project. Can be accessed with git config

You should always set the below variables:

git config --global user.name "Vinayak Lokhande"
git config --global user.email "lokhande.vinayak@gmail.com"

Optionally, you can set the editor you want to use with git:

git config --global core.editor emacs

---
### Git commands in action:

- We will be using a repo named "repo1" which has only readme.md file in it.
- Contents of .git/config file (note the user.name, we will need later in the example):
```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = https://github.com/vinlok/repo1.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[user]
	name = vinlok
```
- Lets create a new file with some content in it: 
```
$cat > sample.txt <<EOF
heredoc> From vinlok
heredoc> EOF
$cat sample.txt
From vinlok
```
- Running git status on this repo will show that sample.txt has changed. At this point it is in modfied stage (remmber the three stages of git?)
```
$git status --short
?? sample.txt
```
- Lets move it to next stage which is the "staged/index":
```
$git add sample.txt
$git status --short
A  sample.txt
```
- Lets further move it to next stage which is commited:
git commit -m "Creating sample.txt with content from user vinlok"

- Lets push this file to github server repo.
git push origin master
- At this point you will see this file on the github UI with the above commit message.

### Git commit
It ofter happens that you have commited some changes to early. Now you have edited an file and want to add it to the same commit. Simple:

```
git commit -m "Adding first changes"
# You changed file named sample2.txt and want to add to the above commit
git add sample2.txt
git commit --amend
```


### Resolving conflict

Merge conflicts happen in git when a competing change is made to tha same file by two person at the same time. Below are some of the examples of merge conflicts and how to resolve them:

##### Example 1:
So you forgot to do a git pull and you have your changes commited. or after you did a git pull some one else edited the same line and pushed to HEAD. Sounds familiar ? :)

- To see this in action, lets do this, create a new directory vinrock and clone the repo1 under it. Once, done, run the git config user.name vinrock for this repo:
```
$mkdir vinrock
$git clone https://github.com/vinlok/repo1.git
$cd repo1
$git config user.name vinrock
$git config user.name
vinrock
```
- Here, we have created another user name vinrock who is going to work with user vinrock.

#### As vinlok/repo1
- Now go back to vinlok/repo1 and add "Text from vinlok" to sample.txt as below:
```
From vinlok
Text from vinlok
```
- Push these changes. Now the HEAD will have the sample.txt with the above content.

#### As vinrock/repo1
- So we are not doing a git pull, hence, the content of sample.txt is as below:
```
From vinlok
```
- Lets change the content of sample.txt in vinrock/repo1.
```
$echo "Text from vinrock" >> sample2.txt
$git add sample.txt
$git commit -m "edit from vinrock"
$git push
```

-  And you will get the below error:
```
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/vinlok/repo1.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
- The above error is suggesting to do a git pull.

- Lets do a git pull and it will show the below error:
```
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/vinlok/repo1
   fd90c60..d958876  master     -> origin/master
Auto-merging sample.txt
CONFLICT (content): Merge conflict in sample.txt
Automatic merge failed; fix conflicts and then commit the result.
```
- However git pull would have edited your file with the below content:
```
<<<<<<< HEAD
Text from vinrock
=======
Text from vinlok
>>>>>>> bccddd36650f678c18598f35b1500bd2722ad49b
```

- Lets dicipher the above. The text above "========" is what vinrock has added and the text below that is what is present on HEAD.
- Open the file in your favourite text editor, remove the lines with <<<<, ===== and >>>>, then keep the text you want to be in the file.
- Do a git add sample.txt and git commit -m "Resolved the conflict on line no 2" and a git push.

#### Example 2:

- You did a git pull and are editing a given file. In the meanwhile some one else has deleted the file in HEAD.
- Lets see this in action. Lets add a file named sample2.txt and keep both vinlok/repo1 and vinrock/repo1 in sync. So, both repos will have below files:
```
$ls
README.md   sample.txt  sample2.txt
```
- Now in vinlok/repo1 delete sample2.txt and push the changes to HEAD.

- Now in vinrock/repo1, WITHOUT git pull, edit the sample2.txt and do a git push to HEAD. You will get the same error as metioned above. Now, do a git pull, the error shown will be different:
```
remote: Counting objects: 2, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 2 (delta 1), reused 2 (delta 1), pack-reused 0
Unpacking objects: 100% (2/2), done.
From https://github.com/vinlok/repo1
   6fd95ad..51e5331  master     -> origin/master
CONFLICT (modify/delete): sample2.txt deleted in 51e5331fb829b6b4d4d61e4096769837f4c37937 and modified in HEAD. Version HEAD of sample2.txt left in tree.
Automatic merge failed; fix conflicts and then commit the result.
```
- You have two options either remove this file and add this file to git and then push. Either can be down as below:
```
git add sample2.txt
or
git remove sample2.txt
```

- Doing a git push after deciding either to keep or remove will fix the issue.
```
git rm sample2.txt
git add -A; git commit -m "Removing sample2 txt as its gone"; git push
```

Reference: https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/

### Git log

- Git has very power way to see the history. Below are the most commonly used commands to see the git history:

1. Plain and simple: git log
2. To see a one liner summary: 
```
git log --pretty=oneline
````
3. To see commits from a particular user: 
```
git log --author=vinlok or git log --author=vinlok --pretty=oneline
```
4. Some thing fancy: 
```
git log --graph --oneline --decorate --all
```
5. To limit history to show only last 'n' commits, use: 
```
git log -2
```
6. Very useful, To see changes in each commit, use -p: 
```
git log -p -2 
```
7. To see logs from past two weeks: 
```
git log --since=2.weeks
```
More details can be found here: https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History

### Branching

Braching is git is used to develop code/features isolated from different user. The idea here is to get the latest code from HEAD and then branch out locally. Now you have luxury to work on two braches: HEAD and the new branch you have created.

- This is how you create a branch:
```
git pull #to get the latest code
git checkout -b vintestbranch
git add -A; git commit -m "some code for vintestbranchcode.txt";
git push origin vintestbranch
git checkout master
```

### Tagging
-Tagging is way by which you can name/version a given checkout. This makes it simple to refer to in git:
```
git tag 1.0.0 git tag 1.1.2 054bd86eea20eb99ae171f1b1722ef1978b2ac12
git tag 1.1.3 8c06a69a57c412554f0ad7912145f14821662fb3
```
- Git tags are *not* pushed unless you explicitly push them using git push --tags:
```
git push tags
```
- Now these tags will be visible in git web UI or available publicly.
