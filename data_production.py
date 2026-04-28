import pandas as pd
import time

df = pd.read_csv("data/power_streaming_data.csv")

for i in range(20):

    sample_df = df.sample(5)

    sample_df.to_csv(
        f"stream_output/batch_{i}.csv",
        index=False
    )

    print(f"Wrote batch {i}")

    time.sleep(10)