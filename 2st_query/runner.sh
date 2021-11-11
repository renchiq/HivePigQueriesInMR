#!/bin/bash

hdfs dfs -rm -r queries/output/2st_query

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Queries Job via Streaming" \
-files `pwd`/mapper.py,`pwd`/reducer.py \
-input queries/input/workersInput \
-output queries/output/2st_query \
-mapper `pwd`/mapper.py \
-reducer `pwd`/reducer.py
