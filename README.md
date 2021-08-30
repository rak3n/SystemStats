# Zenatix Assingment:
As per the assingment repo consists of the following files:
* Python Code for collection System stats, for which i used psutil python library.
* ElasticSearch [Model file](./elasticSearchModel.txt) to signifying the model.
* Kibana Dashboard json exported [file](./kibana-dashboards.2021-08-29-18-16-53.json).
* [Images](./images) of Kibana Dashboard.

# Python Code:
* Python Code consists of two modules, [elasticSearch.py](./elasticSearch.py) and [process_info.py](./process_info.py).
* with [process_info.py](./process_info.py) being entry-point for the application.


# Checklist of Tasks:
* Added  Python code to get information related to processes present in the system.
* Added the list in elasticsearch DB using elasticsearch python client.
* Visualized elaticsearch data, based on cpu and memory percentage usage, grouped by PID's in Kibana Dashboard.
* Also Performed filtering to get only those PID's having CPU usage or memory consumption more than or equal 40%.


# Kibana Dashboard Images
Kibana Dashboard with denoting CPU and memory usage in percentage for all the PID.<br>
![Kibana Dashboard 1](.images\PID_with_usage.png "Kibana Dashboard Image, for denoting CPU and memory usage for all process")
<br>
<br>
Kibana Dashboard Image, for showing PID, with CPU or memory usage more than 40%<br>
![Kibana Dashboard 2](.images\PID_more_Than_40%.png "Kibana Dashboard Image, for showing PID, with CPU or memory usage more than 40%")
