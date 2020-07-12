#include <vector>

int score(const std::vector<int>& dice) {
  unsigned cs[7] = {};
  for (auto d : dice)
    cs[d]++;
  return
    cs[1] / 3 * 1000 + cs[6] / 3 * 600 + cs[5] / 3 * 500 +
    cs[4] / 3 * 400 + cs[3] / 3 * 300 + cs[2] / 3 * 200 +
    cs[1] % 3 * 100 + cs[5] % 3 * 50;
}