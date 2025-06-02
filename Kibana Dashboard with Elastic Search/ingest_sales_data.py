from elasticsearch import Elasticsearch, helpers
import pandas as pd

# Elasticsearch connection
es = Elasticsearch("http://localhost:9200")

# Load cleaned CSV
df = pd.read_csv("clean_sales_data.csv")

# Create the index with mapping (optional if already created manually)
if not es.indices.exists(index="sales"):
    es.indices.create(
        index="sales",
        body={
            "mappings": {
                "properties": {
                    "order_id": {"type": "keyword"},
                    "order_date": {"type": "date"},
                    "region": {"type": "keyword"},
                    "state": {"type": "keyword"},
                    "product": {"type": "text"},
                    "category": {"type": "keyword"},
                    "sub_category": {"type": "keyword"},
                    "customer_name": {"type": "text"},
                    "sales": {"type": "double"},
                    "profit": {"type": "double"}
                }
            }
        }
    )
    print("✅ 'sales' index created.")

# Bulk upload to Elasticsearch
def generate_actions(dataframe):
    for _, row in dataframe.iterrows():
        yield {
            "_index": "sales",
            "_source": row.to_dict()
        }

# Ingest data
helpers.bulk(es, generate_actions(df))
print("✅ Sales data successfully indexed into Elasticsearch")
