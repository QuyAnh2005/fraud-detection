from datetime import timedelta

from feast import FeatureView, Field
from feast.stream_feature_view import stream_feature_view
from feast.types import Float32, Int32, String
from pyspark.sql import DataFrame

from data_sources import transaction_stats_batch_source, transaction_stats_stream_source
from entities import transaction

transaction_stats_view = FeatureView(
    name="transaction_stats",
    description="transaction features",
    entities=[transaction],
    ttl=timedelta(days=36500),
    schema=[
        Field(name="type", dtype=String),
        Field(name="amount", dtype=Float32),
        Field(name="nameOrig", dtype=String),
        Field(name="oldbalanceOrg", dtype=Float32),
        Field(name="newbalanceOrig", dtype=Float32),
        Field(name="nameDest", dtype=String),
        Field(name="oldbalanceDest", dtype=Float32),
        Field(name="newbalanceDest", dtype=Float32),
        Field(name="isFraud", dtype=Int32),
        Field(name="isFlaggedFraud", dtype=Int32),
    ],
    online=True,
    source=transaction_stats_batch_source,
    tags={},
    owner="quyanh",
)


@stream_feature_view(
    entities=[transaction],
    ttl=timedelta(days=36500),
    mode="spark",
    schema=[
        Field(name="type", dtype=String),
        Field(name="amount", dtype=Float32),
        Field(name="nameOrig", dtype=String),
        Field(name="oldbalanceOrg", dtype=Float32),
        Field(name="newbalanceOrig", dtype=Float32),
        Field(name="nameDest", dtype=String),
        Field(name="oldbalanceDest", dtype=Float32),
        Field(name="newbalanceDest", dtype=Float32),
        Field(name="isFraud", dtype=Int32),
        Field(name="isFlaggedFraud", dtype=Int32),
    ],
    timestamp_field="step",
    online=True,
    source=transaction_stats_stream_source,
    tags={},
    owner="stream_source_owner@gmail.com",
)
def transaction_stats_stream(df: DataFrame):
    return df
