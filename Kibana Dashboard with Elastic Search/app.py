from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
from urllib.parse import urlencode
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
es = Elasticsearch("http://localhost:9200")

def build_filter_query(params):
    must_clauses = []
    if params.get("region"):
        must_clauses.append({"match": {"region": params.get("region")}})
    if params.get("category"):
        must_clauses.append({"match": {"category": params.get("category")}})
    if params.get("start_date") and params.get("end_date"):
        must_clauses.append({
            "range": {
                "order_date": {
                    "gte": params.get("start_date"),
                    "lte": params.get("end_date")
                }
            }
        })

    if params.get("profit_filter") == "profit":
        must_clauses.append({"range": {"profit": {"gt": 0}}})
    elif params.get("profit_filter") == "loss":
        must_clauses.append({"range": {"profit": {"lt": 0}}})

    return {"bool": {"must": must_clauses}} if must_clauses else {"match_all": {}}

@app.route("/")
def home():
    return render_template(
        "index.html",
        params={},
        sales=[],
        page=1,
        total_pages=1,
        query_string="",
        profit_count=0,
        loss_count=0,
        chart_labels=[],
        chart_data=[]
    )


@app.route("/search", methods=["GET"])
def search():
    params = request.args.to_dict()
    page = int(params.get("page", 1))
    size = 100

    query = {
        "from": (page - 1) * size,
        "size": size,
        "query": build_filter_query(params)
    }

    try:
        res = es.search(index="sales", body=query)
        hits = res["hits"]["hits"]
        total_hits = res["hits"]["total"]["value"]
        sales = [hit["_source"] for hit in hits]
    except Exception as e:
        return render_template("index.html", error=str(e), sales=[], page=1, total_pages=1, params=params)

    total_pages = max(1, (total_hits + size - 1) // size)

    profit_count = sum(1 for sale in sales if sale.get("profit", 0) > 0)
    loss_count = sum(1 for sale in sales if sale.get("profit", 0) < 0)

    sales_by_month = defaultdict(float)
    for sale in sales:
        try:
            month = datetime.strptime(sale["order_date"], "%Y-%m-%d").strftime("%Y-%m")
            sales_by_month[month] += sale.get("sales", 0)
        except Exception:
            continue

    sorted_months = sorted(sales_by_month)
    sales_data = [sales_by_month[m] for m in sorted_months]

    query_string = urlencode({k: v for k, v in params.items() if k != "page"})

    return render_template(
        "index.html",
        sales=sales,
        page=page,
        total_pages=total_pages,
        params=params,
        query_string=query_string,
        profit_count=profit_count,
        loss_count=loss_count,
        chart_labels=sorted_months,
        chart_data=sales_data,
    )

@app.route("/api/sales_by_category")
def sales_by_category():
    try:
        body = {
            "size": 0,
            "aggs": {
                "sales_by_category": {
                    "terms": {
                        "field": "category",  # ✅ 'category' is already keyword type
                        "size": 10
                    },
                    "aggs": {
                        "total_sales": {
                            "sum": {
                                "field": "sales"
                            }
                        }
                    }
                }
            }
        }

        res = es.search(index="sales", body=body)
        buckets = res["aggregations"]["sales_by_category"]["buckets"]
        data = {
            "labels": [bucket["key"] for bucket in buckets],
            "sales": [round(bucket["total_sales"]["value"], 2) for bucket in buckets]
        }
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/sales_by_region")
def sales_by_region():
    body = {
        "size": 0,
        "aggs": {
            "sales_by_region": {
                "terms": {
                    "field": "region",
                    "size": 10
                },
                "aggs": {
                    "total_sales": {
                        "sum": {
                            "field": "sales"
                        }
                    }
                }
            }
        }
    }

    res = es.search(index="sales", body=body)
    buckets = res["aggregations"]["sales_by_region"]["buckets"]
    data = {
        "labels": [bucket["key"] for bucket in buckets],
        "sales": [round(bucket["total_sales"]["value"], 2) for bucket in buckets]
    }
    return jsonify(data)


    
@app.route("/api/debug")
def debug():
    res = es.search(index="sales", size=1)
    return jsonify(res["hits"]["hits"][0]["_source"])


if __name__ == "__main__":
    app.run(debug=True)
