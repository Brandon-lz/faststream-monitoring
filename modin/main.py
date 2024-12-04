# import modin.pandas as pd
# # import urllib.request
# # url_path = "https://modin-datasets.intel.com/green-taxi/green_tripdata_2015-01.csv"
# # urllib.request.urlretrieve(url_path, "taxi.csv")

# df = pd.read_csv("taxi.csv", parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"], quoting=3)


# import modin.config as modin_cfg
# from distributed import Client

# modin_cfg.Engine.put("dask")
# client = Client('localhost:8786')

# print("connected to cluster successfully!")

# # import urllib.request
# # url_path = "https://modin-datasets.intel.com/green-taxi/green_tripdata_2015-01.csv"
# # urllib.request.urlretrieve(url_path, "taxi.csv")
# # To run this notebook as done in the README GIFs, you must first locally download the 2015 NYC Taxi Trip Data.

# from modin.config import BenchmarkMode
# BenchmarkMode.put(True)


# for i in range(100):
#     isnull = df.isnull()

#     rounded_trip_distance = df[["pickup_longitude"]].applymap(round)
#     print("rounded_trip_distance")




# # pdm run dask scheduler --port=8786 --dashboard-address=:8787
# # pdm run dask worker localhost:8786 --no-dashboard


import modin.pandas as pd
import modin.config as modin_cfg
import time

from distributed import Client



# client = Client(cluster)
# Or use an IP address connection if the cluster instance is unavailable:
client = Client(f"localhost:8687")

client.wait_for_workers(2)
client.ncores()

# 在远程集群中安装依赖
# from dask.distributed import PipInstall
# client.register_plugin(PipInstall(packages=["modin"]))

if __name__ == "__main__":

    modin_cfg.Engine.put("dask")
    # from dask.distributed import Client
    # client = Client(n_workers=6)
    # from distributed import Client
    # client = Client('localhost:8786')

    print("connected to cluster successfully!")

    df = pd.read_csv("https://modin-datasets.intel.com/green-taxi/green_tripdata_2015-01.csv", parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"], quoting=3)

    t0 = time.time()
    for i in range(20):
        isnull = df.isnull()

        rounded_trip_distance = df[["pickup_longitude"]].applymap(round)
        print("rounded_trip_distance")

    print("消耗时间",time.time()-t0)



# pdm run dask scheduler --port=8786 --dashboard-address=:8787
# pdm run dask worker localhost:8786 --no-dashboard