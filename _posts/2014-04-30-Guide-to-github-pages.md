---
layout: post
title: "Github Pages in less than 30 mins!"
date: 2017-4-01
excerpt_separator: <!--more-->
---

My previous blog site was traditional one running on a LAMP stack powered by Joomla. While it did suffice need of typical blog site(and helped to scratch my itch to host my own server/site), the cost of maintaining it ($AWS$) and MySql etc forced me to moved to a new platform. Given the benifits offered by Github pages, it was the obvious choice here.

I did not find the documentation on the github pages site that intuitive. It took me quite sometime to get grasp of things and get going. So I decided to write up this blog so that I can refer to it if needed :)

<!--more-->

# The gist:

1. Jekyll : A static web page generator. To "KISS", you create templates for you webpages, post and then write pages using "Markdown". Jekyll server will take care of converting the markdown to html format and render them. So, you style your pages once and Jekyll will take care of the rest.


2. Github: The pages you created in step 1, are then served by github via jekyll in background.


# Steps:

Git hub pages now offer pre-defined templates to style your website. These are probably the best and fastest way to create Github Pages Site. However, you will loose flexibility of styling your site. Steps below are to create github pages site from scratch, without using github template. I have used CSS to style my pages and have modified some of the CSS templates from W3School.


1. Setup a local jekyll server. Install jekyll as below:
gem install jekyll bundler
bundle exec jekyll site create
jekyll serve

At this point, you should be able to access your site locally on default port of 4000.


2. You can now use the traditional CSS styles to style your website. Just google for CSS templates and there are many to choose from!

3. You can now add various blogs and sections to your site. Refer to this awesome blog: http://jmcglone.com/guides/github-pages/

4. Once you are satisfied with your site locally, you are ready to push it to github pages. Create a new repo in your github account by name: <youname>.github.io. Goto settings, and enable "github pages site" option for this repo.

5. Push the locally created site to the master branch of this repo.

6. And you are all set! Github pages might take few mins to get your site ready. Once ready, you should be able to access it as : <youname>.github.io

#### References:

- https://jekyllrb.com/docs/posts/
- http://jmcglone.com/guides/github-pages/