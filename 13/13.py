lines = open("in.txt").read().splitlines()
ans = sum(map(int, lines))
open("out.txt", "w").write(str(ans)[:10])
