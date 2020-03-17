#!/bin/sh
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/sbin/start-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave
/usr/local/hadoop/bin/hdfs dfs -rm -r /1a/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /1a/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /1a/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /project1/part1/parking-violations-data/Parking_Violations.csv* /1a/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /project1/part1/1a/mapper.py -mapper /project1/part1/1a/mapper.py \
-file /project1/part1/1a/reducer.py -reducer /project1/part1/1a/reducer.py \
-input /1a/input/* -output /1a/output/
/usr/local/hadoop/bin/hdfs dfs -cat /1a/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /1a/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /1a/output/
/usr/local/hadoop/sbin/stop-dfs.sh
/usr/local/hadoop/sbin/stop-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh stop historyserver