---
layout: post
title: "Getting started with Ruby"
date: 2017-05-25
categories: ['Programming']
excerpt_separator: <!--more-->
---

Ruby is amazing language being very expressive language backed up by a very strong and active community. However, getting a particular version of Ruby running is bit of challenge. There are various ways to get Ruby going, below I am documenting the way which has always worked for me


<!--more-->
Below are the pre-requisites:

Ruby Installer:
ruby-install: https://github.com/postmodern/ruby-install#readme

Ruby Manager:
chruby: https://github.com/postmodern/chruby#readme

### Steps:

Below steps are for MAC.

1. First step is to setup the ruby-install on your system. Just copy paste the below on mac terminal:
```
wget -O ruby-install-0.6.1.tar.gz https://github.com/postmodern/ruby-install/archive/v0.6.1.tar.gz
tar -xzvf ruby-install-0.6.1.tar.gz
cd ruby-install-0.6.1/
sudo make install
```

2. Next is to setup chruby:
```
wget -O chruby-0.3.9.tar.gz https://github.com/postmodern/chruby/archive/v0.3.9.tar.gz
tar -xzvf chruby-0.3.9.tar.gz
cd chruby-0.3.9/
sudo make install
```
This might take some time depending on the packages it needs to compile for your system.

3. Now that you have ruby-install, install the version you need:
```
ruby-install ruby-2.2.5
ruby-install ruby-x.x.x
```

4. Now we will use chruby to change to the version you want. Before that, you need to get chruby sourced. You can add this to your bashprofile so that you do not have to worry about this again:
```
source /usr/local/opt/chruby/share/chruby/auto.sh;
source /usr/local/share/chruby/chruby.sh
```

5. Now you can list the versions of Ruby installed just by running chruby. Use the below command to change to the version you want:
```
$chruby                                                                                                           
ruby-2.2.5
$chruby ruby-2.2.5
$ruby --version
ruby 2.2.5p319 (2016-04-26 revision 54774) [x86_64-darwin16]
```

Thats it!