import argparse

def compute_lps_array(pattern):
    lps = list()
    lps.append(0)
    prefix_last_matched_idx = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[prefix_last_matched_idx]:
            prefix_last_matched_idx += 1
            lps.append(prefix_last_matched_idx)
            i += 1

        elif prefix_last_matched_idx != 0:
            prefix_last_matched_idx = lps[prefix_last_matched_idx-1]
        else:
            lps.append(0)
            i += 1
    return lps


def kmp_search(pattern, txt):
    results = []
    lps = compute_lps_array(pattern)
    txt_idx = 0
    pattern_idx = 0
    while txt_idx < len(txt):

        if txt[txt_idx] == pattern[pattern_idx]:
            txt_idx += 1
            pattern_idx += 1
            if pattern_idx == len(pattern):  # complete match discovered
                results.append((txt_idx-pattern_idx, txt_idx))
                pattern_idx = lps[pattern_idx-1]

        else:  # where lps is useful

            if pattern_idx != 0:
                pattern_idx = lps[pattern_idx-1]
            else:
                txt_idx += 1

    return results


def main(args):
    print(kmp_search(args.pattern, args.text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Argument Parser for KMP search algorithm")
    parser.add_argument("-p", "--pattern", type=str, required=True)
    parser.add_argument("-t", "--text", type=str, required=True)
    args = parser.parse_args()
    main(args)
