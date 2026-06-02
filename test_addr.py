import pandas as pd
df = pd.read_csv("docs/서울특별시_전월세가_2023.csv", nrows=5)
def make_address(row):
    addr = f"서울특별시 {row['자치구명']} {row['법정동명']}"
    bon = row.get('본번', None)
    bu = row.get('부번', None)
    if pd.notnull(bon) and str(bon).strip() != "":
        bon_str = str(int(bon)) if isinstance(bon, float) or isinstance(bon, int) else str(bon)
        addr += f" {bon_str}"
        if pd.notnull(bu) and str(bu).strip() != "" and float(bu) > 0:
            bu_str = str(int(bu)) if isinstance(bu, float) or isinstance(bu, int) else str(bu)
            addr += f"-{bu_str}"
    return addr
df['주소'] = df.apply(make_address, axis=1)
print(df[['자치구명', '법정동명', '본번', '부번', '주소']])
