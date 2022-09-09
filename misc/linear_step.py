import dataclasses


@dataclasses.dataclass
class LinearFeedStep:
    start_rate: float
    end_rate: float
    duration_s: float

start_rates = [0.0045, 0.0190, 0.0210]
end_rates = [0.0190, 0.0210, 0.0210]
durations = [5.6, 1.0, 100.0]
feed_rates = {
    "feed_start_rate": start_rates,
    "feed_end_rate": end_rates,
    "feed_durations": durations,  # last is large to allow for a longer feed
}
steps = [
    LinearFeedStep(
        feed_rates["feed_start_rate"][i],
        feed_rates["feed_end_rate"][i],
        feed_rates["feed_durations"][i] * 60 * 60,
    )
    for i in range(len(feed_rates["feed_start_rate"]))
]

def start_linear_feed(steps: list[LinearFeedStep]):
    """
    Output: [{'start_rate': 0.0045, 'end_rate': 0.019, 'duration': 20160.0}, 
            {'start_rate': 0.019, 'end_rate': 0.021, 'duration': 3600.0}, 
            {'start_rate': 0.021, 'end_rate': 0.021, 'duration': 360000.0}
    ]
    """
    schedule = [
            {
                "start_rate": step.start_rate,
                "end_rate": step.end_rate,
                "duration": step.duration_s,
            }
            for step in steps
        ]
    print(schedule)



if __name__ == "__main__":
    start_linear_feed(steps)