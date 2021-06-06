## Api End Point Details 
The end point for all the DBS's follow the below generic 
format 
1.http://localhost:5000/{db_type}/create_table
2.http://localhost:5000/{db_type}/insert_table_data
3.http://localhost:5000/{db_type}/update_table_data
4.http://localhost:5000/{db_type}/delete_table_data
5.http://localhost:5000/{db_type}/bulk_insert_data
6.http://localhost:5000/{db_type}/view_table_data

The corresponding payload for the POST requests.
## Create Table MySQL:
{
    "table_name": "emp",
    "columns": [
        "emp_id",
        "emp_name",
        "emp_city"
    ],
    "data_types" : ["integer PRIMARY KEY","varchar(255)","varchar(255)"]
}
## *MySQL DB*
## Insert Data MySQL:
{
    "table_name": "emp",
    "columns": [
        "emp_id",
        "emp_name",
        "emp_city"
    ],
    "values": [
        2,
        "Priyanka",
        "Singapore"
    ]
}
## Update Data MySQL: 
{
    "table_name": "emp",
    "columns": [
        "emp_name",
        "emp_city"
    ],
    "values": [
        "Rishaan3" ,
        "Hydrabad"  
    ],
    "condition" : "where emp_id=2"
}
## Delete Data MySQL: 
{
    "table_name": "emp",
    "condition": "where emp_id=3"
}
## Bulk Insert data MySQL:
{
    "table_name": "emp",
    "file_name": "emp_data.csv"
}
## DownLoad Data MySQL:
{
    "table_name": "emp"
}

## *Cassendra DB*
## Create Table Cassendra :
{
    "table_name": "emp",
    "columns": [
        "emp_id ",
        "emp_name",
        "emp_city"
    ],
    "data_types" : ["int PRIMARY KEY","text","text"]
} 
## Insert Table Data Cassendra:
{
    "table_name": "emp",
    "columns": [
        "emp_id",
        "emp_name",
        "emp_city"
    ],
    "values": [
         "2",
        "Priyanka",
        "Singapore"
    ]
}
## Update Table Data Cassendra :
{
    "table_name": "emp",
    "columns": [
        "emp_name",
        "emp_city"
    ],
    "values": [
        "Rishaan3" ,
        "Hydrabad"  
    ],
    "condition" : "where emp_id='2'"
}
## Delete Table Data Cassendra:
{
    "table_name": "emp",
    "condition": "where emp_id=3"
}
## Bulk Insert data Cassendra:
{
    "table_name": "emp",
    "file_name": "emp_data.csv"
}
## DownLoad Data Cassendra:
{
    "table_name": "emp"
}
## *Mongo DB*
## Insert Data Mongo DB
{
    "emp_id": " 1",
    "emp_name": "Rahul",
    "emp_city": "Pune"
}
## Update Data Mongo DB
{
    "query_str": {
        "emp_name": "Rahul Banerjee"
    },
    "value_str": {
        "$set": {
            "emp_city": "Rahul"
        }
    }
}
## Delete Data Mongo DB
{
    "emp_name": {
        "$eq": "Rahul"
    }
}
## Bulk Insert data Mongo DB:
{
    "table_name": "emp",
    "file_name": "emp_data.csv"
}
## DownLoad Data  Mongo DB:
{
    "table_name": "emp"
}
