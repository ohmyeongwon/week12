import pandas as pd


def 정제(df):
    정제_df = df.copy()

    # 점수가 비어 있는 행을 삭제한다.
    정제_df = 정제_df.dropna(subset=["점수"]).copy()
    print("빈 점수 삭제 후:", len(정제_df))

    # 모든 열이 완전히 같은 중복 행을 삭제한다.
    정제_df = 정제_df.drop_duplicates().copy()
    print("중복 행 삭제 후:", len(정제_df))

    # 반과 과목 값의 앞뒤 공백을 제거한다.
    정제_df["반"] = 정제_df["반"].str.strip()
    정제_df["과목"] = 정제_df["과목"].str.strip()
    print("공백 제거 후:", len(정제_df))

    # 점수가 0~100 범위를 벗어난 행을 삭제한다.
    정제_df = 정제_df[정제_df["점수"].between(0, 100)].copy()
    print("점수 범위 확인 후:", len(정제_df))

    return 정제_df


def 반별평균(df):
    반별_점수 = df.groupby("반")["점수"]
    통계표 = 반별_점수.agg(["count", "mean", "median", "max"]).round(2)

    # 반별 점수 통계표를 출력한다.
    print(통계표)

    # 반 이름을 인덱스로 하고 반올림된 평균을 값으로 반환한다.
    return 통계표["mean"]


if __name__ == "__main__":
    원본_df = pd.read_csv("scores_2026.csv")
    df = 정제(원본_df)

    # 과목이 수학인 행만 남긴다.
    수학_df = df[df["과목"] == "수학"]
    print("수학 행 수:", len(수학_df))

    # 1반이면서 90점 이상인 행만 남긴다.
    고득점_1반_df = df[(df["반"] == "1반") & (df["점수"] >= 90)]
    print("1반 90점 이상 행 수:", len(고득점_1반_df))

    # 반별 점수 평균을 계산한다.
    반별_평균 = df.groupby("반")["점수"].mean()
    print(반별_평균)

    # 과목과 반별 점수 평균을 계산한다.
    과목_반별_평균 = df.groupby(["과목", "반"])["점수"].mean()
    print(과목_반별_평균)

    # 반별 통계표를 출력하고 평균값을 반환한다.
    print(반별평균(df))