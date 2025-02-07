from feast import FeatureService

from features import *

feature_service = FeatureService(
    name="model_v1",
    features=[driver_hourly_stats_view[["conv_rate"]]],
    owner="gursoy@yerli.org",
)

feature_service_2 = FeatureService(
    name="model_v2", 
    features=[driver_hourly_stats_view], 
    owner="gursoy@yerli.org",
)
