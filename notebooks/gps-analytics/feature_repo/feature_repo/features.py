from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32
from datetime import timedelta

# Entity
entity = Entity(
    name="entity_id",
    join_keys=["entity_id"],
)

# Data source
feature_source = FileSource(
    path="data/features.parquet",
    event_timestamp_column="event_timestamp",
)

# Feature view
lag_features = FeatureView(
    name="lag_features",
    entities=[entity],
    ttl=timedelta(days=1),
    schema=[
        Field(name="lag_count", dtype=Float32),
    ],
    source=feature_source,
)