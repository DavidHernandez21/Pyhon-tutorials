from multiprocessing import cpu_count
from multiprocessing import Pool

import numpy as np
import pandas as pd


@pd.api.extensions.register_dataframe_accessor('apply_parallel')
@pd.api.extensions.register_series_accessor('apply_parallel')
class ApplyParallel:
    """Registers a custom method `apply_parallel` for dataframes & series."""

    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def __call__(self, func, axis=0):
        """Applies func to a pandas object along the axis.
        Useful with big pandas objects when func can't be easily vectorized.
        func can't be a lambda function because multiprocessing can't pickle it.
        """
        # df.apply(func, axis=1) applies func to each row,
        # but np.array_split(df, n, axis=0) splits df into n chunks of rows,
        # so swap the axis number when working with dataframes.
        if isinstance(self._obj, pd.DataFrame):
            axis = 1 - axis
        # But if the pandas object is a series, the axis is always 0.
        else:
            assert axis == 0
        # Use all the CPUs
        num_jobs = cpu_count()
        with Pool(num_jobs) as p:
            # Split your pandas object into chunks
            split_objects = np.array_split(self._obj, num_jobs, axis=axis)
            # Map your function to each split in parallel
            results = p.map(func, split_objects)
        # Concat them back together
        return pd.concat(results)


df = pd.DataFrame({'col': list(range(30))})


def my_func(row):
    return row.col**2


assert all(df.apply_parallel(my_func, axis=1) == df.apply(my_func, axis=1))
