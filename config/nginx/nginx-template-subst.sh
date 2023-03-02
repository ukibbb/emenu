#!/usr/bin/env bash

# exports env var DNS_SERVER with the value of the first nameserver IP address listed in /etc/resolv.conf
export DNS_SERVER=$(cat /etc/resolv.conf |grep -i '^nameserver'|head -n1|cut -d ' ' -f2)
# substitutes the values of DEV_ENV and DNS_SERVER in /var/nginx.conf and writes resulting configuration to /etc/nginx/conf.d/default.conf
# envsubst is a utility that substitutes the values of environment variables in a template file.
# The $ sign is used to reference the variables, and the variables are enclosed in single quotes to prevent the shell from expanding them.
envsubst '$DNS_SERVER' < /var/nginx.conf > /etc/nginx/conf.d/default.conf
