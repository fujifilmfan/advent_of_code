from itertools import count


reports = []

with open("2024_day2_input.txt") as f:
    for line in f:
        line.rstrip("\n")
        report = [int(x) for x in line.split(" ")]
        reports.append(report)

safe_rpts = []
unsafe_rpts = []


def report_is_safe(r: list) -> bool:
    diffs = [r[i + 1] - r[i] for i in range(len(r) - 1)]
    if all(0 < diff < 4 for diff in diffs) or all(-4 < diff < 0 for diff in diffs):
        return True
    return False


for rpt in reports:
    safe_rpts.append(rpt) if report_is_safe(rpt) else unsafe_rpts.append(rpt)

print(len(safe_rpts))  # 639 <-- correct
print(len(unsafe_rpts))

safe_rpts_w_prob_dampener = []
unsafe_rpts_w_prob_dampener = []


def report_is_safe_with_prob_dampener(r: list) -> bool:
    """Remove both levels around a problem to see if it makes the report safe."""
    diffs = [r[i + 1] - r[i] for i in range(len(rpt) - 1)]
    for i, diff in enumerate(diffs):
        if diff < 1 or diff > 3 or diff > -1 or diff < -3:
            rpt_wo_i = [lvl for j, lvl in enumerate(rpt) if j != i]
            rpt_wo_i_plus_1 = [lvl for j, lvl in enumerate(rpt) if j != i + 1]
            if report_is_safe(rpt_wo_i) or report_is_safe(rpt_wo_i_plus_1):
                return True
    return False


for rpt in unsafe_rpts:
    safe_rpts_w_prob_dampener.append(rpt) if report_is_safe_with_prob_dampener(
        rpt
    ) else unsafe_rpts_w_prob_dampener.append(rpt)


print(len(safe_rpts_w_prob_dampener))  # 674 <-- correct
print(len(unsafe_rpts_w_prob_dampener))

print(f"Total safe reports: {len(safe_rpts) + len(safe_rpts_w_prob_dampener)}")
