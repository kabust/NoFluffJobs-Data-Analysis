import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.axes import Axes


def apply_bar_counters(series: pd.Series) -> None:
    for i in range(len(series)):
        plt.text(i, series.iloc[i] + (series.iloc[0] * 0.01), series.iloc[i], ha="center")


def make_autopct(values):
    def autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f"{pct:.2f}%\n({val:d})"
    return autopct


def plot_technologies(
        df: pd.DataFrame,
        axs: Axes,
        x: int,
        y: int,
        category: str | None = None,
        amount: int = 10
) -> None:
    if category:
        must_haves = df[df["Category"] == category]["Must haves"]
        axs[x, y].set_title(category)
    else:
        must_haves = df["Must haves"]
        axs[x, y].set_title("All categories")

    must_haves = must_haves.str.split(",").explode()
    must_haves = must_haves.value_counts().sort_values(ascending=False)

    must_haves_labels = must_haves.index.to_list()[1:amount + 1]
    must_haves_values = must_haves[1:amount + 1]

    axs[x, y].bar(must_haves_labels, must_haves_values)
    axs[x, y].tick_params("x", labelrotation=45)