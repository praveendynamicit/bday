from django.shortcuts import render
import pandas as pd
from datetime import datetime

# Create your views here.
from django.views.decorators.clickjacking import xframe_options_exempt
import re
import datetime




@xframe_options_exempt
def index(request):
    def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

    df = pd.read_csv('dataset.csv')

    base = datetime.datetime.today()
    date_list = []
    tod = datetime.datetime.now()
    d = datetime.timedelta(days = 2)
    a = tod - d
    for x in range(0,2):
        date = str(a - datetime.timedelta(days=x))
        date = date.split(' ')
        date_list.append(change_date_format(date[0]))
    for x in range(0, 5):
        date = str(base + datetime.timedelta(days=x))
        date = date.split(' ')
        date_list.append(change_date_format(date[0]))

    df1 = df[df['Date of Birth'].isin(date_list)]

    df1['Date'] = pd.to_datetime(df1["Date of Birth"])

    # df_sorted_data = df.sort_values(by='Date')

    # df_sorted_data_top5 = df.head(5)

    from datetime import date
    today = date.today()
    today = str(today)

    # df_sorted_data_top5["Date"] = df_sorte_ddata_top5["Date"].astype(str)

    df1["Date"] = df1["Date"].astype(str)

    df1.loc[df1['Date'] == today, 'Date'] = "Today"

    df1_list = df1.values.tolist()

    context = {"data":df1_list}

    return render(request,'index.html',context)