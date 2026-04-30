import pandas as pd
import time

# read in power streaming data
df = pd.read_csv("data/power_streaming_data.csv")

for i in range(20):

    # take random sample of 5 values
    sample_df = df.sample(5)

    # output sample to folder
    sample_df.to_csv(
        f"stream_output/batch_{i}.csv",
        index=False
    )

    print(f"Wrote batch {i}")

    # wait for 10 seconds before next iteration
    time.sleep(10)