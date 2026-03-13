# Daylight Savings ⏰
# Codédex

def calculate_sleep_debt(planned, actual):
  sleep_debt = 0

  streak = 0
  longest_streak = 0

  for i in range(len(planned)):
    gap = planned[i] - actual[i]

    if gap > 0:
      sleep_debt += gap
      streak += 1

      if longest_streak < streak:
        longest_streak = streak
    else:
      streak = 0

  sleep_debt += 1

  return sleep_debt, longest_streak
