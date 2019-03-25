#include <types.h>

/*
  S(k, n) ~ return the number of
            partitions of a k-set
            into n blocks 

          ~ unordered distribution
            of k distinct balls into 
            n identical bins where each 
            bin has at least one ball
*/
uintll S(uintll k, uintll n){

  if (k == n) return 1;
  else if (k > n) return 0;
  else if (k < n && n == 0) return 0;
  return S(k - 1, n - 1) + n*S(k - 1, n);

}

/*
  B(n) ~ returns the number of
         partitions (of any size)
         of an n-set

*/
uintll B(uintll n){

  uintll k = 1;
  uintll res = 0;
  for (; k <= nl k ++)
    res += S(n, k);

  return res;
}

/*
  b(n, k) ~ returns the binomial
            coefficient { n \choose k }

          ~ number of distributions
            of k identical balls to 
            n distinct bins such that each bin
            has at most one ball
*/
uintll b(n, k){

  if (n == k) return 1;
  else if (k > n) return 0;
  else if (k < n && k == 0) return 1;
  return b(n - 1, k - 1) + b(n - 1, k);
}

/*
  multi(n, k) ~ returns number of distributions
                of k identical balls to n
                distinct bins (no restrictions)

*/
uintll multi(n, k){

  return b(n + k - 1, k);

}
