import os.path
import time
from functools import partial
from multiprocessing import Pool

import numpy as np
import scipy.io.wavfile


def gen_fake_data(filenames: list[str], folder_name: str):

    try:
        os.mkdir(folder_name)
        print('generating fake data')
    except FileExistsError:
        pass

    for filename in filenames:  # homework: convert this loop to pool too!
        if not os.path.exists(filename):
            print(f'creating {filename}')
            gen_wav_file(filename, frequency=440, duration=60.0 * 4)


def gen_fake_data_multiprocessing(
    filenames: list[str],
    folder_name: str,
    chunk_size: int,
):

    try:
        os.mkdir(folder_name)
        print('generating fake data')
    except FileExistsError:
        pass

    gen_fake_files_partial = partial(gen_fake_files, frequency=440, duration=60.0 * 4)
    with Pool() as pool:
        results = pool.imap_unordered(
            gen_fake_files_partial,
            filenames,
            chunksize=chunk_size,
        )

        [print(filename) for filename in results]


def gen_fake_files(filename: str, frequency: float, duration: float) -> str:
    if os.path.exists(filename):
        return f'{filename} already exists'
    # print(f"creating {filename}")
    return f'{gen_wav_file(filename, frequency=frequency, duration=duration)} created'


def gen_wav_file(filename: str, frequency: float, duration: float) -> str:
    samplerate = 44100
    t = np.linspace(0.0, duration, int(duration * samplerate))
    data = np.sin(2.0 * np.pi * frequency * t) * 0.0
    scipy.io.wavfile.write(filename, samplerate, data.astype(np.float32))
    return filename


def etl(filename: str) -> tuple[str, float]:
    # extract
    start_t = time.perf_counter()
    samplerate, data = scipy.io.wavfile.read(filename)

    # do some transform
    eps = 0.1
    data += np.random.normal(scale=eps, size=len(data))
    data = np.clip(data, -1.0, 1.0)

    # load (store new form)
    new_filename = f'{filename.removesuffix(".wav")}-transformed.wav'
    scipy.io.wavfile.write(new_filename, samplerate, data)
    end_t = time.perf_counter()

    return filename, end_t - start_t


def etl_demo(num_of_files: int, chunk_size: int, folder_name: str = 'sounds'):
    filenames = [
        os.path.join(folder_name, f'example{n}.wav') for n in range(num_of_files)
    ]

    start_time = time.perf_counter()
    # gen_fake_data(filenames, folder_name)
    gen_fake_data_multiprocessing(filenames, folder_name, chunk_size)
    print(
        f'generated {num_of_files} files in {time.perf_counter() - start_time:.2f} seconds',
    )
    start_t = time.perf_counter()

    print('starting etl')
    with Pool() as pool:
        results = pool.imap_unordered(etl, filenames, chunksize=chunk_size)

        for filename, duration in results:
            print(f'{filename} completed in {duration:.2f}s')

    end_t = time.perf_counter()
    total_duration = end_t - start_t
    print(f'etl took {total_duration:.2f}s total')


def main():

    etl_demo(num_of_files=24, chunk_size=1)


if __name__ == '__main__':
    main()
