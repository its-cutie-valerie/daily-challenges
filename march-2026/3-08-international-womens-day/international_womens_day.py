# International Women's Day 💖
# Codédex

def analyze(percentages):  
  net_change = 0
  trend = '' 
  dips = 0

  # ====== Net Change Per Year ======
  
  net_change = (percentages[-1] - percentages[0]) / (len(percentages) - 1)  

  # ====== Trend ======
  
  last_three_avg = sum(percentages[-3:]) / 3
  first_three_avg = sum(percentages[:3]) / 3
  
  if last_three_avg > first_three_avg:
    trend = 'improving'
  elif last_three_avg == first_three_avg:
    trend = 'stagnating'
  else:
    trend = 'declining'
  
  # ====== Dips ======
  
  for i in range(len(percentages)-1):
    if percentages[i+1] < percentages[i]:
      dips = dips + 1
  
  return round(net_change, 4), trend, dips
