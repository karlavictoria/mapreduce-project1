#!/bin/sh
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/sbin/start-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave
/usr/local/hadoop/bin/hdfs dfs -rm -r /2a/round1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2a/round1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2a/round2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /2a/round1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /project1/part2/nba-data/shot_logs.csv* /2a/round1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /project1/part2/2a/round1/mapper.py -mapper /project1/part2/2a/round1/mapper.py \
-file /project1/part2/2a/round1/reducer.py -reducer /project1/part2/2a/round1/reducer.py \
-input /2a/round1/input/* -output /2a/round1/output/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /project1/part2/2a/round2/mapper.py -mapper /project1/part2/2a/round2/mapper.py \
-file /project1/part2/2a/round2/reducer.py -reducer /project1/part2/2a/round2/reducer.py \
-input /2a/round1/output/part-00000* -output /2a/round2/output/
/usr/local/hadoop/bin/hdfs dfs -cat /2a/round2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /2a/round1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2a/round1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2a/round2/output/
/usr/local/hadoop/sbin/stop-dfs.sh
/usr/local/hadoop/sbin/stop-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh stop historyserver