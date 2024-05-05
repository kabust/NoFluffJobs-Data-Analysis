import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from analysis.utils import (
    apply_bar_counters,
    make_autopct,
    plot_technologies,
    choose_technology,
)


CHOICE = choose_technology()


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df[
        df["Must haves"].apply(
            lambda x: not isinstance(x, float) and CHOICE in x
        )
    ]

    df["Salary (mean)"] = (df["Bottom salary"] + df["Top salary"]) / 2
    df = df[~df["Salary (mean)"].isna()]

    return df


def plot_categories(df: pd.DataFrame) -> None:
    categories = df["Category"].value_counts().sort_values(ascending=False)

    plt.figure(figsize=(10, 8))
    plt.bar(categories.index.to_list(), height=categories, width=0.8)
    plt.xticks(rotation=90)
    plt.title("Categories by popularity")
    plt.ylabel("Amount of vacancies")
    plt.xlabel("Categories")
    plt.subplots_adjust(bottom=0.25)

    apply_bar_counters(categories)

    plt.savefig(f"analysis/plots/{CHOICE}/category_plot.png")
    plt.show()


def plot_remote_non_remote(df: pd.DataFrame) -> None:
    remotes_count = df["Remote"].value_counts()

    labels = ["Remote", "Non remote only"]
    plt.pie(remotes_count, labels=labels, autopct=make_autopct(remotes_count))
    plt.title("Possibilities to work remotely")

    plt.savefig(f"analysis/plots/{CHOICE}/remote_non_remote_plot.png")
    plt.show()


def plot_salaries_by_seniority(df: pd.DataFrame) -> None:
    seniority_count = df["Seniority"].value_counts().sort_values(ascending=False)
    salaries_by_seniority = (
        df.groupby("Seniority")
        .mean("Salary (mean)")["Salary (mean)"]
        .astype(int)
        .sort_values(ascending=False)
    )

    labels = df["Seniority"].unique()
    plt.bar(labels, salaries_by_seniority)
    plt.bar(labels, seniority_count * 100)

    plt.title("Mean salary by seniority")
    plt.ylabel("Salary, PLN Gross")
    plt.xlabel("Seniority / Number of vacancies")

    apply_bar_counters(seniority_count)
    apply_bar_counters(salaries_by_seniority)

    plt.savefig(f"analysis/plots/{CHOICE}/salaries_by_seniority_plot.png")
    plt.show()


def plot_salaries_by_category(df: pd.DataFrame) -> None:
    salaries_by_category = (
        df.groupby("Category")
        .mean("Salary (mean)")["Salary (mean)"]
        .astype(int)
        .sort_values(ascending=False)
    )

    labels = salaries_by_category.index.to_list()

    plt.figure(figsize=(12, 8))
    plt.bar(labels, salaries_by_category)

    plt.title("Mean salary by category")
    plt.ylabel("Salary, PLN Gross")
    plt.xlabel("Category")
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.3)

    apply_bar_counters(salaries_by_category)

    plt.savefig(f"analysis/plots/{CHOICE}/salaries_by_category_plot.png")
    plt.show()


def plot_top_technologies_by_categories(df: pd.DataFrame) -> None:
    categories = df["Category"].value_counts().sort_values(ascending=False).index.to_list()[:5]

    fig, axs = plt.subplots(3, 2)
    fig.set_size_inches(14, 12)
    fig.suptitle(f"Top 10 technologies required by 5 most popular categories (except {CHOICE})")

    plot_technologies(df, axs, 0, 0)
    plot_technologies(df, axs, 0, 1, categories[0])
    plot_technologies(df, axs, 1, 0, categories[1])
    plot_technologies(df, axs, 1, 1, categories[2])
    plot_technologies(df, axs, 2, 0, categories[3])
    plot_technologies(df, axs, 2, 1, categories[4])

    fig.tight_layout(pad=1.5)

    plt.savefig(f"analysis/plots/{CHOICE}/top_technologies_by_categories_plot.png")
    plt.show()


def main():
    try:
        df = pd.read_csv(f"analysis/{CHOICE}.csv")
    except FileNotFoundError:
        print(f"File '{CHOICE}.csv' wasn't found, check that file is located in the same directory")
        return

    df = clean_df(df)

    plot_categories(df)
    plot_remote_non_remote(df)
    plot_salaries_by_seniority(df)
    plot_salaries_by_category(df)
    plot_top_technologies_by_categories(df)


if __name__ == "__main__":
    main()
