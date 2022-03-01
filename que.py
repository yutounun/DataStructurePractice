max = 6
que = [0] * max
head = 0
tail = 0

def enque(d):
  global tail
  # tail = 0 1週目
  # tail = 1 2週目
  # nt = 1 1週目
  # nt = 2 2週目
  nt = (tail+1)%max

  if nt == head:
    print("これ以上データは入りません")
  else:
    # que[0] = 0 1週目
    # que[1] = 1 2週目
    que[tail] = d
    # tail = 1 1週目
    # tail = 2 2週目
    tail = nt
    print(d, "を追加した")

def deque():
  global head
  if head == tail:
    print("取り出すデータがありません")
    return None
  else:
    # 最初から順に取り出していく
    d = que[head]
    # head pointerを後ろにずらす
    head = (head+1)%max
    return d

for i in range(6):
  enque(i)

for i in range(6):
  d = deque()
  print(d,"を取り出した")