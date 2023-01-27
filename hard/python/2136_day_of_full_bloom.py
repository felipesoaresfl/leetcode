'''
You have n flower seeds. Every seed must be planted first before it
can begin to grow, then bloom. Planting a seed takes time and so does
the growth of a seed. You are given two 0-indexed integer arrays plantTime
and growTime, of length n each:

plantTime[i] is the number of full days it takes you to plant the ith seed.
Every day, you can work on planting exactly one seed. You do not have to
work on planting the same seed on consecutive days, but the planting of
a seed is not complete until you have worked plantTime[i] days on planting
it in total.
growTime[i] is the number of full days it takes the ith seed to grow after
being completely planted. After the last day of its growth, the flower blooms
and stays bloomed forever.
From the beginning of day 0, you can plant the seeds in any order.

Return the earliest possible day where all seeds are blooming.

To understand better with examples, visit the link:

https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
'''


class Solution(object):
    def earliestFullBloom(plantTime, growTime):
        day_today = 0
        days_all_bloom = 0

        plant_grow_time = zip(growTime, plantTime)
        plant_grow_time = sorted(plant_grow_time, reverse=True)
        # plant first who takes the longest to grow

        for time_grow, time_plant in plant_grow_time:
            days_all_bloom = max(days_all_bloom, (day_today +
                                                  time_plant + time_grow))
            day_today += time_plant
        return days_all_bloom
    print(earliestFullBloom([1, 4, 3], [2, 3, 1]))
