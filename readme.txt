in docker:
1) docker pull sequenceiq/hadoop-docker:2.7.1
2) docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash

outside docker:
1) docker cp sample.csv DOCKER_NAME:/sample.csv
2) docker cp map_1.py DOCKER_NAME:/map_1.py
3) docker cp reduce_1.py DOCKER_NAME:/reduce_1.py
4) docker cp map_2.py DOCKER_NAME:/map_1.py
5) docker cp reduce_2.py DOCKER_NAME:/reduce_2.py
6) docker cp map_3.py DOCKER_NAME:/map_3.py
7) docker cp reduce_3.py DOCKER_NAME:/reduce_3.py

in docker:
1) cd $HADOOP_PREFIX
2) bin/hdfs dfs -mkdir data
3) bin/hdfs dfs -put sample.csv data

in docker run map-reduce:
1) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample/ -output data_output/out_1 -mapper map_1.py -reducer reduce_1.py -file /map_1.py -file /reduce_1.py
2) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input data_output/out_1 -output data_output/out_2 -mapper map_2.py  -reducer reduce_2.py -file /map_2.py -file /reduce_2.py
3) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input data_output/out_2 -input data_output/out_3 -output sample_output/prepare_prodtime -mapper map_3.py  -reducer reduce_3.py -file /map_3.py -file /reduce_3.py