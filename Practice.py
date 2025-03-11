import pandas as pd

file_path = "TCB_2018_2020.csv"

def load_data():
    return pd.read_csv(file_path)

#(1)
def print_all_data(df):
    return df

#(2)
def filter_by_close(df, x, y):
    filtered_df = df[(df['Close'] < x) | (df['Close'] > y)]
    return filtered_df

#(3)
def extract_selected_columns(df, x, y):
    return df.loc[x:y, ['Date', 'High', 'Low']]

#(4)
def export_transaction_date(df, date):
    result = df[df['Date'] == date]
    return result

#(5)
def filter_by_dates(df, dates):
    return df[df['Date'].isin(dates)]


if __name__ == "__main__":
    df = load_data()

    # 1
    print(df)

    # 2
    x = float(input("Nhập giá trị x: "))
    y = float(input("Nhập giá trị y: "))
    print(filter_by_close(df, x, y))

    # 3
    start_index = int(input("Nhập chỉ mục bắt đầu: "))
    end_index = int(input("Nhập chỉ mục kết thúc: "))
    print(extract_selected_columns(df, start_index, end_index))

    # 4
    date = input("Nhập ngày giao dịch (YYYY-MM-DD): ")
    print(export_transaction_date(df, date))

    # 5
    dates_list = input("Nhập danh sách ngày (phân tách bằng dấu phẩy): ").split(',')
    print(filter_by_dates(df, dates_list))
