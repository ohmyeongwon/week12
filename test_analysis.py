import pandas as pd

from analysis import 정제, 반별평균


# 각 CSV 파일을 한 번씩 읽고 정제한다.
scores_원본 = pd.read_csv("scores_2026.csv")
mini_원본 = pd.read_csv("mini.csv")

scores_df = 정제(scores_원본)
mini_df = 정제(mini_원본)


def test_scores_정제_후_100행():
    assert len(scores_df) == 100


def test_반_종류가_1반과_2반뿐이다():
    assert set(scores_df["반"].unique()) == {"1반", "2반"}


def test_반별_점수_합계가_전체_합계와_같다():
    반별_합계 = scores_df.groupby("반")["점수"].sum()
    assert 반별_합계.sum() == scores_df["점수"].sum()


def test_mini의_1반_평균이_80이다():
    assert 반별평균(mini_df)["1반"] == 80.0