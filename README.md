Q: Briefly describe the GDP development of these different countries over the years
A: The US maintains its number one spot as largest country in the world regarding GDP.
When rebasing the time series to 2000, we can easily see that China has grown at the fastest accelerated pace.
Out of the 7 countries, all of them except Japan show decent signs of growth over the time period.

Q: When you added your .gitignore to your repo to ignore .csv files, was the file indeed ignored?
A: The file that had already been uploaded previously was not removed. However, when I added a test csv file, this was ignored. So .gitignore acts going forward, not retroactively.

Q: Why do we have to add additional_dependencies to mypy in the .pre-commit-config.yaml?
A: mypy requires types-seaborn, polars, pandas-stubs and matplotlib to run, so this checks they are installed first.
