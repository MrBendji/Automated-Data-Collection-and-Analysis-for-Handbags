#import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 24),
    'retries': 1,
    'retry_delay': timedelta(minutes=5), 
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

test_dag = DAG('fashionsearch_dag', default_args=default_args, schedule=timedelta(days=1))  

# This task deletes all json files which are generated in previous scraping sessions
# t1 = BashOperator(
#     task_id='delete_json_files',
#     bash_command='run_delete_files',
#     dag=dag)  


# This task runs the spider for www.derimod.com
# And populates the related json file with data scraped
t2 = BashOperator(
    task_id='derimod_spider',
    bash_command='./run_derimod_spider.sh',
    dag=test_dag)  


# This task runs the spider for www.hepsiburada.com
# And populates the related json file with data scraped
t3 = BashOperator(
    task_id='hepsiburada_spider',
    bash_command='./run_hepsiburada_spider.sh',
    dag=test_dag)  

# This task runs the spider for www.hm.com
# And populates the related json file with data scraped
t4 = BashOperator(
    task_id='hm_spider',
    bash_command='./run_hm_spider.sh',
    dag=test_dag)  


# This task runs the spider for www.koton.com
# And populates the related json file with data scraped
t5 = BashOperator(
    task_id='koton_spider',
    bash_command='./run_koton_spider.sh',
    dag=test_dag)  


# This task checks and removes null line items in json files
t6 = BashOperator(
    task_id='prep_jsons',
    bash_command='./run_prep_jsons.sh',
    dag=test_dag)  

# This task checks and removes dublicate line items in json files
t7 = BashOperator(
    task_id='delete_dublicate_lines',
    bash_command='./run_del_dub_lines.sh',
    dag=test_dag)  

# This task populates the remote ES clusters with the data inside the JSON files
# t8 = BashOperator(
#     task_id='json_to_elasticsearch',
#     bash_command='run_json_to_es',
#     dag=dag)  

# With sequential executer, all tasks depends on previous task
# No paralell task execution is possible
# Use local executer at least for paralell task execution
t2 >> t3 >> t4 >> t5 >> t6 >> t7