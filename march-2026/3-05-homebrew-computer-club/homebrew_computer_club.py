# Homebrew Computer Club 🤓
# Codédex

def dompier_music(switches):
  # Write code below 💖
  result = []

  for i in range(len(switches)):
    decimal = 0

    for j in range(len(switches[i])):
      if switches[i][j] == '1':
        decimal = decimal + 2 ** (9-int(j))

    if decimal == 261:
      result.append("C4")
    elif decimal == 294:
      result.append("D4")
    elif decimal == 329:
      result.append("E4")
    elif decimal == 349:
      result.append("F4")
    elif decimal == 392:
      result.append("G4")
    elif decimal == 440:
      result.append("A4")
    elif decimal == 494:
      result.append("B4")
    elif decimal == 523:
      result.append("C5")
    else:
      result.append("REST")

  return result
