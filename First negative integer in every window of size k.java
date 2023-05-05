class Compute {
    public long[] printFirstNegativeInteger(long a[], int n, int k)
    {
        long[] r = new long[n - k + 1];
        int c = 0;
        Queue<Long> q = new LinkedList<>();

        int l = 0;
        for (int m = 0; m< n; m++) {
            if (a[m] < 0) {
                q.add(a[m]);
            }

            if (m - l + 1 == k) {
                if (q.isEmpty()) {
                    r[c++] = 0;
                } else {
                    long num = q.peek();
                    r[c++] = num;
                    if (num == a[i]) {
                        q.remove();
                    }
                }
                l++;
            }
        }

        return r;
    }
}