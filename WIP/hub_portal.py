#
import streamlit as st
import pandas as pd
import datetime
import pytimeparse
from dateutil.parser import parse
from ocs_academic_hub import HubClient
import plotly.express as px
import time
import base64

st.title('Hub Data View Portal - v0.95')


@st.cache(allow_output_mutation=True)
def hub_client():
    hub_ocs = HubClient()
    hub_ocs.refresh_datasets(
        experimental=True,
        additional_status="eds_onboarding",
    )
    return hub_ocs


@st.cache(show_spinner=False)
def get_data_view(dataset, asset, start_time, end_time, interpolation):
    return hub.dataview_interpolated_pd(hub.namespace_of(dataset),
                                        hub.asset_dataviews(filter='', asset=asset)[0],
                                        start_time.isoformat(), end_time.isoformat(), interpolation)


def get_table_download_link_csv(df):
    csv = df.to_csv(index=False).encode()
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="dataview.csv" target="_blank">Download CSV file</a>'
    return href


with st.form(key='dataset'):
    hub = hub_client()
    dataset = st.selectbox("Step 1: Select dataset", hub.datasets(),
                           help="Check datasets info at https://academic.osisoft.com/datasets")
    submit_button = st.form_submit_button(label='Submit')

with st.form(key='asset-dv'):
    hub.set_dataset(dataset)
    asset = st.selectbox('Step 2: Select asset', hub.assets()["Asset_Id"],
                         help="For asset info check URL")
    start = st.text_input("Step 3: Start time", "2021-05-07T20:03:35", None, "start-time",
                          "default",
                          "Start time for CSV result using ISO 8601 time format https://en.wikipedia.org/wiki/ISO_8601")
    window = st.text_input("Step 4: Time window", "240 mins", None, "window-time", "default",
                           "CSV results will end at start time + this time window, supported format " +
                           "https://github.com/wroberts/pytimeparse#pytimeparse-time-expression-parser")
    interpolation = st.text_input("Step 5: Interpolation period (format is HH:MM:SS)", "00:00:01", None,
                                  "interpolation", "default", "Interpolation interval with format HH:MM:SS")
    csv_button = st.form_submit_button(label='Step 6: Click for CSV')

start_time = parse(start)
delta = datetime.timedelta(seconds=pytimeparse.parse(window))
end_time = start_time + delta

st.write("Current dataset: ", dataset, " || Selected asset:", asset)
st.write("Start time:", start_time.isoformat(), "||", "End time :", end_time.isoformat())
st.write("Interpolation interval (HH:MM:SS):", interpolation)
st.write("OCS namespace:", hub.namespace_of(dataset), "||", "Default data view ID:",
         hub.asset_dataviews(filter="", asset=asset)[0])

if 'df' not in globals():
    df = pd.DataFrame()

if csv_button:
    with st.spinner(text='Getting CSV from OCS Data View...'):
        df = get_data_view(dataset, asset, start_time, end_time, interpolation)
    st.success('Data View Request Complete!!')
    st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)

st.write(df)

with st.form(key="plot"):
    plot_button = st.form_submit_button(label="(Optional step) Click here for line plot")

if plot_button:
    df = get_data_view(dataset, asset, start_time, end_time, interpolation)
    st.write("Data line plot")
    with st.spinner(text='Plotting data...'):
        columns = list(df.select_dtypes(include='number').columns)
        st.write(px.line(df, x="Timestamp", y=columns))
    st.success("Done!")