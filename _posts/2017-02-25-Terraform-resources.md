---
layout: post
title: "Terraform: Most commonly used resources"
date: 2017-03-25
excerpt_separator: <!--more-->
weight: 1000
---

# Terraform resources:

### aws_instance:
<pre>
resource aws_instance "vintest" {
	ami = "ami-12345"
	instance_type = "t2.micro"
	user_data = <<-EOF
				#!/bin/bash
				echo "Put your script you want to be run during cloud init"
				EOF
	tags {
		name = "vintest"
		type = "webserver"
	}
}
</pre>

<!--more-->

### aws_security_group:

<pre>
resource aws_security_group "vin_webserver_security_group" {
	name = "vin_webserver_security_group"
	ingress {
		from_port = 9031
		to_port = 9031
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}
	tags {
		name = "vin_webserver_security_group"
		type = "security_group"
	}	
}
</pre>>

### aws_launch_configuration:
- aws_launch_configuration resource is same like that of aws_instance.
<pre>
resource aws_launch_configuration "vin_lc" {
	ami = "ami-12345"
	instance_type = "t2.micro"
	user_data = <<-EOF
				#!/bin/bash
				echo "Put your script you want to be run during cloud init"
				EOF
	tag {
		name = "vintest"
		type = "webserver"
	}
	lifecycle {
	create_before_destroy = true
	}
}
</pre>

### aws_autoscaling_group:

<pre>

resource aws_autoscaling_group "vin_asg" {
	launch_configuration = "${aws_launch_configuration.vin_lc.id}"
	availablity_zones = ["${data.aws_availability_zones.all.names}"]
	health_check_type= "ELB"
	min_size = 2
	max_size = 4
	tag {
		key = "Name"
		value = "terraform-asg-example"
		propagate_at_launch = true
	}
}
</pre>

### aws_elb:

<pre>

resource aws_elb "vin_elb" {
	name = "vin_elb"
	availablity_zones = ["${data.aws_availability_zones.all.names}"]
	security_groups = ["${aws_security_group.vin_webserver_security_group.id}"]
	listener {
		lb_port = 8001
		lb_protocol = "http"
		instance_port = "${var.server_port}"
		instance_protocol = "http"
	}

	health_check {
		health_threshold = 2
		unhealthy_threshold = 3
		timeout = 3
		interval = 30
		target = "HTTP:${var.server_port}/"
	}
}
</pre>

