from feast import Entity

transaction = Entity(
    name="transaction",
    join_keys=["nameOrig"],
    description="customer who started the transaction",
    tags={},
    owner="quyanh",
)
