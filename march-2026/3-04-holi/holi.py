## Holi 🌈
## Codédex

def find_missing_colors(grid):
  answer = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

  for i in range(7):
    for j in range(7):
      if grid[i][j] in answer:
        answer.remove(grid[i][j])
  return answer