from [this video](https://www.youtube.com/watch?v=ey_P64E34g0) 
python -m cProfile -o log.pstats -m small_funct_in_hot_loop get_sum_of_list

## the profile statistics browser.
python -m pstats log.pstats 
sort cumtime

## yelp-gprof2dot
gprof2dot log.pstats | dot -Tsvg -o log.svg


from [this video](https://www.youtube.com/watch?v=m_a0fN48Alw)
