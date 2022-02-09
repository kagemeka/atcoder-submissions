import typing


# 3

def calc_wind_power(dist: int) -> typing.Union[int, str]:
  assert dist >= 0
  if dist < 15: return 0
  elif dist < 93: return 1
  elif dist < 201: return 2
  elif dist < 327: return 3
  elif dist < 477: return 4
  elif dist < 645: return 5
  elif dist < 831: return 6
  elif dist < 1_029: return 7
  elif dist < 1_245: return 8
  elif dist < 1_467: return 9
  elif dist < 1_707: return 10
  elif dist < 1_959: return 11
  else: return 12


# 22.5
def calc_wind_direction(degree: int) -> str:
  dir = [
    'N', 'NNE', 'NE',
    'ENE', 'E', 'ESE',
    'SE', 'SSE', 'S', 'SSW', 'SW',
    'WSW', 'W', 'WNW',
    'NW', 'NNW',
  ]
  i = (degree * 10 + 1_125) % 3_6000 // 2_250
  return dir[i]




def solve(deg: int, dis: int) -> typing.NoReturn:
  wp = calc_wind_power(dis)
  dir = 'C' if wp == 0 else calc_wind_direction(deg)
  print(dir, wp)


def main() -> typing.NoReturn:
  deg, dis = map(int, input().split())
  solve(deg, dis)



main()
