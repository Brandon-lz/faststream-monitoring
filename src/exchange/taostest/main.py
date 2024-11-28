import taosrest
import time
import random

def tdengine_example()->taosrest.TaosRestConnection:
    client = None
    url="http://localhost:6041"
    reqId = 3
    try:
        client = taosrest.connect(
            url=url,
            user="root",
            password="taosdata",
            timeout=30,
            timezone="Asia/Shanghai",
        )
        print(f"Connected to {url} successfully.")

        # create database
        rowsAffected = client.execute(f"CREATE DATABASE IF NOT EXISTS power")
        print(f"Create database power successfully, rowsAffected: {rowsAffected}")
        
        # create super table
        rowsAffected = client.execute(
            "CREATE TABLE IF NOT EXISTS power.meters (`ts` TIMESTAMP, `current` FLOAT, `voltage` INT, `phase` FLOAT) TAGS (`groupid` INT, `location` BINARY(30))"
        )
        print(f"Create stable power.meters successfully, rowsAffected: {rowsAffected}")

        # insert data
        data = 0.0
        while True:
            data += 0.1*random.randint(-50,100)
            sql = f"""
                INSERT INTO 
                power.d1001 USING power.meters (groupid, location) TAGS(3, "California")
                    VALUES (NOW , {data}, 219, 0.31000) 

                """
            affectedRows = client.execute(sql)
            print(f"Successfully inserted {affectedRows} rows to power.meters.")
            time.sleep(0.5)
            
            # break
        # sql = "SELECT ts, current, location FROM power.meters limit 100"
        sql = "SELECT ts, current, location FROM power.meters limit 100"
        result = client.query(sql)
        for row in result:
            print(f"ts: {row[0]}, current: {row[1]}, location:  {row[2]}")
        print(f"Successfully queried {result.code} rows from power.meters.")

        # delete data
        # client.execute("DELETE FROM power.meters WHERE ts > '2021-10-01 00:00:00.000'")


        # drop database
        # rowsAffected = client.sql(f"DROP DATABASE IF EXISTS power")
        # print(f"Drop database power successfully, rowsAffected: {rowsAffected}")

    except Exception as err:
        print(f"error raised in {url} , ErrMessage:{err}")
    finally:
        if client:
            client.close() 

if __name__ == "__main__":
    tdengine_example()