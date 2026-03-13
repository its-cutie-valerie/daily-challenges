## Blood Moon 🩸
## Codédex

def blood_moon(time):
  # Write code below 💖

  hrs_string, min_string = time.split(":")
  result = []
  
  hrs = int(hrs_string)
  min = int(min_string)

  # print(hrs)
  # print(min)
  
  # ====== first one ====== 

  hrs = hrs + 2
  min = min + 48

  if min > 60:
    min = min - 60
    hrs = hrs + 1
  
  if hrs > 24:
    hrs = hrs - 24
  
  result.append(f"{hrs:02d}:{min:02d}")

  # ====== second one ====== 

  hrs = hrs + 2
  min = min + 48

  if min > 60:
    min = min - 60
    hrs = hrs + 1

  if hrs > 24:
    hrs = hrs - 24
  
  result.append(f"{hrs:02d}:{min:02d}")

  # ====== third one ====== 

  hrs = hrs + 2
  min = min + 48

  if min > 60:
    min = min - 60
    hrs = hrs + 1
  
  if hrs > 24:
    hrs = hrs - 24
  
  result.append(f"{hrs:02d}:{min:02d}")

  return result