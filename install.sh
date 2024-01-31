#!/bin/bash
apt-get update && apt-get install -y default-jdk


export JAVA_HOME=/usr/lib/jvm/default-java
export PATH=$PATH:$JAVA_HOME/bin

java -version