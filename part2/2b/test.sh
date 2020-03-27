!/bin/bash
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/sbin/start-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/MR/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/round1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/round2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /2b/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /project1/part2/nba-data/shot_logs.csv* /2b/input/
   
for i in {1..10}
do
    if (($i == 1));then     
        /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
        -file /project1/part2/2b/MR/round1/mapper.py -mapper /project1/part2/2b/MR/round1/mapper.py \
        -file /project1/part2/2b/MR/round1/reducer.py -reducer /project1/part2/2b/MR/round1/reducer.py \
        -input /2b/input/* -output /2b/MR/output/
        centroids=$(/usr/local/hadoop/bin/hdfs dfs -cat /2b/MR/output/part-00000 | head -n 1)
        echo "$centroids"
    else
        /usr/local/hadoop/bin/hdfs dfs -rm -r /2b/MR/output/
        /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
        -file /project1/part2/2b/MR/roundn/mapper.py -mapper "/project1/part2/2b/MR/roundn/mapper.py $centroids" \
        -file /project1/part2/2b/MR/roundn/reducer.py -reducer /project1/part2/2b/MR/roundn/reducer.py \
        -input /2b/input/* -output /2b/MR/output/
        centroids=$(/usr/local/hadoop/bin/hdfs dfs -cat /2b/MR/output/part-00000)
        echo "$centroids"
    fi
done
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/MR/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /2b/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /project1/part2/nba-data/shot_logs.csv* /2b/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /project1/part2/2b/round1/mapper.py -mapper "/project1/part2/2b/round1/mapper.py $centroids" \
-file /project1/part2/2b/round1/reducer.py -reducer /project1/part2/2b/round1/reducer.py \
-input /2b/input/* -output /2b/round1/output/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /project1/part2/2b/round2/mapper.py -mapper /project1/part2/2b/round2/mapper.py \
-file /project1/part2/2b/round2/reducer.py -reducer /project1/part2/2b/round2/reducer.py \
-input /2b/round1/output/part-00000* -output /2b/round2/output/
/usr/local/hadoop/bin/hdfs dfs -cat /2b/round2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/round1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /2b/round2/output/
/usr/local/hadoop/sbin/stop-dfs.sh
/usr/local/hadoop/sbin/stop-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh stop historyserver