**What exactly is the Deschutes Dataset?**

-   Read the [Deschutes Dataset
    Description](https://data.academic.osisoft.com/nbviewer/github/academic-hub/datasets/blob/master/Brewery_Dataset_Doc.ipynb)
    document

    -   Describes the assets and processes Deschutes uses, along with data
        streams, meta data, and overall shape

    -   Explains the data views, and which ones are available for Deschutes
        Dataset

**If the Deschutes Dataset seems aligned to your interests,**

-   Read through the [Hub Python Library QuickStart Guide Preview
    Version](https://data.academic.osisoft.com/nbviewer/github/academic-hub/datasets/blob/master/Hub_Library_Quickstart.ipynb)

**Teacher’s Assistant (TA) Guidebook**

-   The [TA
    Guidebook](https://academichub.blob.core.windows.net/hub/OSIsoft%20Academic%20Hub%20-%20TA%20Guidebook%20-%20General%20Distribution.pdf)
    contains step by step instructions for a TA setting up a course to use the
    Academic Hub, including sections for:

    -   Software and Security Requirements

    -   Classroom Administration

    -   Academic Hub Account Creation Workflow

    -   Data Access Examples for Community Datasets

    -   Guidance for Contributing Datasets to the Academic Hub

**We created curriculum based on the Deschutes Dataset, as a Jupyter Notebook
with three exercises**

-   [Exercise 1: Apparent Degree of
    Fermentation](https://data.academic.osisoft.com/nbviewer/url/localhost:8000/DESCHUTES_GUIDE.ipynb#exercise1)

    In this learning module, students analyze the Apparent Degree of
    Fermentation (ADF) during the beer-making process, which is a critical
    process parameter that informs brewers how much a batch has fermented over
    time. Through this exercise, students will learn how to build predictive
    linear and predictive piecewise linear models on ADF.

-   [Exercise 2: Beer Cooling
    Prediction](https://data.academic.osisoft.com/nbviewer/url/localhost:8000/DESCHUTES_GUIDE.ipynb#exercise2)

    In this learning module, students visualize and analyze the data, and build
    the predictive model of the cooling temperature. Consistent cooling
    temperature profile of every batch is directly related to the quality of
    beer production.

-   [Exercise 3: Principal Component Analysis
    (PCA)](https://data.academic.osisoft.com/nbviewer/url/localhost:8000/DESCHUTES_GUIDE.ipynb#exercise3)

    In the learning module, students use PCA to determine the anomalous
    production batch, and the contributing factors for such deviation behavior.
    Principal Component Analysis is a statistical technique that compresses the
    dimensionality of large datasets to a few Principal Components to represent
    the data.

-   Here you can view the entire [Deschutes Dataset
    curriculum](https://data.academic.osisoft.com/nbviewer/url/localhost:8000/DESCHUTES_GUIDE.ipynb)

**If you are already familiar with either Jupyter Notebooks or Python, you can
download the Hub Python Library QuickStart Guide and explore the dataset. If you
want to use Google Collab environment to run the QuickStart notebook, please
skip to the Jupyter Notebook within Collab section.**

# Jupyter Notebook Download

-   If you already have Jupyter Notebook (Anaconda3) installed on your machine,
    you can download and run the Hub Python Library QuickStart Guide after you
    have created an OSIsoft Academic Hub Account

    1.  Create an OSIsoft Academic Hub (OSIsoft Cloud Services) Account using
        the [Account Registration](https://academic.osisoft.com/individual)

        -   OSIsoft will send an email to you acknowledging OSIsoft Cloud
            Services Account creation

            -   *OSIsoft Cloud Services Account creation process is not
                automated nor instant, due to required verification*

                -   The email will come from cloudservices\@osisoft.com

                -   You need to click on the acceptance link, boxed in red below

                -   Please note – every invitation expires after 21 days!

                ![](media/ef6ae0018ae6bf116dfd2bc43e4eba3e.png)

        1.  Open up Jupyter Notebook in your browser

        2.  Click on the download version of the [Hub Python Library QuickStart
            Guide Jupyter Download
            Version](https://academichub.blob.core.windows.net/hub/Hub_Library_Quickstart.ipynb)

        3.  Navigate to <http://localhost:8888/tree> and to your Downloads
            folder (or wherever your default Downloads are stored)

        4.  Click on the “Hub_Library_Quickstart.ipynb” Jupyter Notebook, which
            will open up in a new browser tab

        5.  You are now able to click through and run the various Python code
            samples demonstrating how to navigate through the Deschutes Brewery
            Dataset

# Python Script Download

-   If you are already using Python on your machine, you can download and run
    the Hub Python Library QuickStart Guide after you have created an OSIsoft
    Academic Hub Account

    1.  Create an OSIsoft Academic Hub (OSIsoft Cloud Services) Account using
        the [Account Registration](https://academic.osisoft.com/individual)

        -   OSIsoft will send an email to you acknowledging OSIsoft Cloud
            Services Account creation

            -   *OSIsoft Cloud Services Account creation process is not
                automated nor instant, due to required verification*

                -   The email will come from cloudservices\@osisoft.com

                -   You need to click on the acceptance link, boxed in red below

                -   Please note – every invitation expires after 21 days!

                ![](media/ef6ae0018ae6bf116dfd2bc43e4eba3e.png)

        1.  Click on the [Python
            script](https://academichub.blob.core.windows.net/hub/Hub_Library_Quickstart.py)
            (version \>= 3.6)

        2.  Before running the script, execute: pip install ocs_academic_hub

        3.  You are now able to run the various Python code samples
            demonstrating how to navigate through the Deschutes Brewery Dataset

# Jupyter Notebook within Collab

-   The current authentication mechanism using an Academic Hub Account only
    works for locally run notebook. In the case of Collab (or other hosted
    notebook service) another mechanism based on a configuration file containing
    a client ID and secret must be used.

    -   Click the following link to run the notebook:
        <https://colab.research.google.com/github/academic-hub/datasets/blob/master/Hub_Library_Quickstart-CMU.ipynb>

    -   Upload the configuration you received from OSIsoft in the root directory
        of Collab:  
        

        ![](media/5768ca8c2b8f9fc2a8c1c54ea87f75f9.png)

    -   Run the cells in sequence up to the HubClient cell. Before running it,
        make sure that the uploaded configuration filename and the one assigned
        to environment variable OCS_HUB_CONFIG match:  
        

        ![](media/3c1e97220f59f383325e27807c0eb1dd.png)

    -   If authentication is successful, you should see the message “---
        authorization granted --“.

Jenny Danielsen

![](media/2bfcb8ceb5893abdbb0a691cf21b0cd3.png)

Academic Account Manager \| OSIsoft \| Energy Tower IV, Suite 1200 \| Houston,
TX 77079

Mobile 281.881.2464 \| Email: jdanielsen\@osisoft.com

![](media/aa3b958cece743458e49a8884172612f.png)

![](media/0c235949e1b34699ae45154f7ffb0f9d.png)

![](media/3aa8fcc581ba68982a62ed30e6786f14.png)

![](media/d538ed68792b203283c7518b9dc7a397.png)

![](media/347960dac00f09ca8dabeefc1ac1a37b.png)

Notice: This message and any files or text attached to it are intended only for
the recipients named above and contain information that may be confidential or
privileged. If you are not an intended recipient, you must not forward, copy,
use or otherwise disclose this communication or the information contained
herein. In the event you have received this message in error, please notify the
sender immediately by replying to this message, and then delete all copies of it
from your system. Thank you.
