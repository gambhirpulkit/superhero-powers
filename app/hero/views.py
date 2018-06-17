import pandas as pd
import matplotlib.pyplot as plt

from django.shortcuts import render


def visualize_data(request):

    info_file = "../heroes_information.csv"
    power_file = "../super_hero_powers.csv"
    context = {}

    df_info = pd.read_csv(info_file)
    df_power = pd.read_csv(power_file)

    outer_merge_df = pd.merge(df_info, df_power, left_on='name', right_on='hero_names', how='outer')

    # I'm not a superhero fan so I assume superheroes with same name and different features are different. No offense.
    total_heroes = len(outer_merge_df[['name', 'hero_names']])
    # unique_heroes = len(pd.unique(outer_merge_df[['name', 'hero_names']].values.ravel('K')))

    shared_powers = 0
    unique_powers = 0
    for col in df_power.columns[1:]:
        if df_power.sum()[col] > 1:
            shared_powers += 1
        elif df_power.sum()[col] == 1:
            unique_powers += 1

    sf_power = df_power.sum().drop('hero_names')
    # Plot line chart using this data frame
    df_line_chart = pd.DataFrame({'power': sf_power.index, 'frequency': sf_power.values})

    # line_fig = plt.figure()
    # line_fig.savefig('line_figure.png')

    df_bar_chart = pd.merge(df_info, df_power, left_on='name', right_on='hero_names', how='inner')

    context["total_heroes"] = total_heroes
    context["unique_powers"] = unique_powers
    context["shared_powers"] = shared_powers
    return render(request, 'dashboard/index.html', context)