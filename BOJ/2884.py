H, M = map(int, input().split())
if M >= 45:
  print(f'{H} {M-45}')
else:
  if H == 0:
    print(f'{24-1} {60-(45-M)}')
  else:
    print(f'{H-1} {60-(45-M)}')
