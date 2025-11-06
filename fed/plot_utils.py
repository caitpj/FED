# fed/plot_utils.py
from __future__ import annotations


import pandas as pd
import matplotlib.pyplot as plt

# import your helpers from the local package
from fed.data import convert_csv_to_dataframe, wide_to_long


def load_gdp_long(file_path: str) -> pd.DataFrame:
    """
    Load the wide GDP CSV and return a tidy long DataFrame
    with columns: Country Name, year (int), gdp (float).
    """
    df = convert_csv_to_dataframe(file_path)
    df = wide_to_long(df)

    # clean types
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df["gdp"] = pd.to_numeric(df["gdp"], errors="coerce")
    df = df.dropna(subset=["year", "gdp"]).copy()
    df["year"] = df["year"].astype(int)
    return df


def filter_countries(
        df_long: pd.DataFrame, countries: list[str]) -> pd.DataFrame:
    """
    Return only the selected countries, preserving the order
    you pass in `countries`.
    """
    df = df_long[df_long["Country Name"].isin(countries)].copy()
    # preserve legend/order
    df["Country Name"] = pd.Categorical(
        df["Country Name"], categories=countries, ordered=True)
    return df.sort_values(["Country Name", "year"])


def plot_gdp_timeseries(
    df_long: pd.DataFrame,
    countries: list[str],
    *,
    title: str | None = None,
    log_scale: bool = False,
    normalize: bool = False,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """
    Plot GDP over time for the given countries.

    Parameters
    ----------
    df_long : long-form DataFrame from `load_gdp_long`
    countries : list of country names to include
    title : optional chart title
    log_scale : if True, use log scale on y-axis
    normalize : if True, index each country's GDP to 100 at first year
    ax : optional Matplotlib Axes to draw on

    Returns
    -------
    ax : Matplotlib Axes
    """
    data = filter_countries(df_long, countries)

    if normalize:
        # index each country's GDP to 100 at its first available year
        data = data.sort_values(["Country Name", "year"]).copy()
        base = data.groupby("Country Name")["gdp"].transform("first")
        data["gdp_index"] = (data["gdp"] / base) * 100
        y_col = "gdp_index"
        y_label = "GDP (index, first year = 100)"
    else:
        y_col = "gdp"
        y_label = "GDP (current US$)"

    if ax is None:
        fig, ax = plt.subplots(figsize=(9, 5))

    for country, sub in data.groupby("Country Name", sort=False):
        ax.plot(sub["year"], sub[y_col], label=str(country))

    ax.set_xlabel("Year")
    ax.set_ylabel(y_label)
    ax.set_xlim(data["year"].min(), data["year"].max())
    if log_scale and not normalize:
        ax.set_yscale("log")
    if title:
        ax.set_title(title)

    ax.grid(True, alpha=0.3)
    ax.legend(title="Country", ncols=2, frameon=False)
    return ax


# fix later
'''
def save_fig(ax: plt.Axes, path: str, dpi: int = 200) -> None:
    """Convenience helper to save the current figure."""
    ax.figure.tight_layout()
    ax.figure.savefig(path, dpi=dpi)
'''
