---
layout: post
title: "S3 Cross account access"
date: 2020-11-23
categories: ['AWS']
excerpt_separator: <!--more-->
---

There are three ways to setup s3 cross account access

## Resource and IAM policy

<img src="http://www.vinayaklokhande.com/images/aws/s3/cross_account_res_IAM.png" alt="S3 Cross Account Access Resource and IAM" />



## Cross Account IAM

<img src="http://www.vinayaklokhande.com/images/aws/s3/cross_account_role.png" alt="S3 Cross Account Access Resource and IAM" />


## S3 ACL and IAM policy.

This is same as #1. Only difference is that instead of S3 bucket policy, S3 Object ACL's are used.