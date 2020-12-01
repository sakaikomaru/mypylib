from StringAlgorithm import SuffixArray

def main():
  S = input()
  n = len(S)

  S = list(map(ord, S + '$'))
  lcp = SuffixArray.lcp_array(S, SuffixArray.suffix_array(S))
  print(n * (n + 1) // 2 - sum(lcp))

if __name__ == "__main__":
  main()