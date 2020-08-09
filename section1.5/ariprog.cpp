/*
ID: ashayp22
PROG: ariprog
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <ctime>
using namespace std;
ifstream fin("ariprog.in");
ofstream fout("ariprog.out");
int prog_len, max_num;
bool set[125001] =
{
  0
};
int bsq[31375], bsq_num = 0, max_bsq;
int ans_num = 0;
struct Answer
{
  int a;
  int b;
}ans[40000];
int
cmp(const void* a, const void* b)
{
  return (*(int *) a - *(int *) b);
}
int
cmp2(const void* a, const void* b)
{
  struct Answer* aa = (Answer*) a;
  struct Answer* bb = (Answer*) b;
  if ((aa->b) != (bb->b))
      return((aa->b) - (bb->b));
  else
      return((aa->a) - (bb->a));
}
void
check(int a, int b)
{
  for (int i = 0; i < prog_len / 2 + 1; i++)
      if (!set[a + b * i] || !set[a + b * (prog_len - 1 - i)])
          return;
  ans[ans_num].a = a;
  ans[ans_num].b = b;
  ans_num++;
}
int
main()
{
  fin >> prog_len >> max_num;
  max_bsq = max_num * max_num * 2;
  for (int p = 0; p <= max_num; p++)
      for (int q = p; q <= max_num; q++)
        {
          int n = p* p + q* q;
          if (!set[n])
            {
              set[n] = true;
              bsq[bsq_num++] = n;
            }
        }
  qsort(bsq, bsq_num, sizeof(bsq[0]), cmp);
  for (int i = 0; i < bsq_num - prog_len + 1; i++)
      for (int j = i + 1; j < bsq_num; j++)
        {
          int a = bsq[i], b = bsq[j] - bsq[i];
          if (a + b * (prog_len - 1) > max_bsq)
              break;
          check(a, b);
        }
  if (ans_num == 0)
      fout << "NONE" << endl;
  else
    {
      qsort(ans, ans_num, sizeof(ans[0]), cmp2);
      for (int i = 0; i < ans_num; i++)
          fout << ans[i].a << ' ' << ans[i].b << endl;
    }
  return 0;
}