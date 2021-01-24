H,W,N,M = map(int, input().split())

image_pixels = []
kernel_pixels = []

new_H, new_W = H-N+1, W-M+1
convoluted_pixels = [[0 for _ in range(new_W)] for _ in range(new_H)]

for _ in range(H):
  pixels = list(map(int, input().split()))
  image_pixels.append(pixels)

# Take in Kernal input and flip rows + columns
for _ in range(N):
  pixels = list(map(int, input().split()))
  kernel_pixels.append(pixels)

for i in range(len(kernel_pixels)):
  kernel_pixels[i] = kernel_pixels[i][::-1]

kernel_pixels = kernel_pixels[::-1]

# Traverse image_pixels with kernal and produce convoluted_pixels
for x in range(new_H):
  for y in range(new_W):
    for i in range(N):
      for j in range(M):
        convoluted_pixels[x][y] += image_pixels[x+i][y+j] * kernel_pixels[i][j]
    
for row in convoluted_pixels:
  for column in row:
    print(column, end=' ')
  print()
