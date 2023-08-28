from datetime import timedelta

from feast import FileSource, KafkaSource
from feast.data_format import JsonFormat, ParquetFormat

transaction_ds_parquet_file = "../data_sources/sample_dataset.parquet"

transaction_stats_batch_source = FileSource(
    name="transaction_dataset",
    file_format=ParquetFormat(),
    path=transaction_ds_parquet_file,
    timestamp_field="step",
    created_timestamp_column="created",
)

transaction_stats_stream_source = KafkaSource(
    name="transaction_dataset_stream",
    kafka_bootstrap_servers="localhost:29092",
    topic="transactions",
    timestamp_field="step",
    batch_source=transaction_stats_batch_source,
    message_format=JsonFormat(
        schema_json="""step integer, type string, amount double,
                    nameOrig string, oldbalanceOrg double,	newbalanceOrig double, 
                    nameDest string, oldbalanceDest double,	newbalanceDest double, 
                    isFraud integer, isFlaggedFraud integer, created timestamp"""
    ),
    watermark_delay_threshold=timedelta(minutes=5),
    description="The Kafka stream containing the transaction stats",
)
