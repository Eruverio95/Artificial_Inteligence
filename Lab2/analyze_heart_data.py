import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def basic_report(df: pd.DataFrame) -> dict:
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'target_distribution': df['target'].value_counts().to_dict() if 'target' in df.columns else {}
    }


if __name__ == '__main__':
    data = load_data("..\\Data\\Heart_Data.csv")
    print(basic_report(data))