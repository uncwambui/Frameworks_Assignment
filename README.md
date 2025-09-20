📊 CORD-19 Frameworks Assignment


-This project explores the CORD-19 research dataset (metadata.csv) and builds a simple Streamlit app to visualize COVID-19 research trends.




🚀 Project Overview 

-The goal of this assignment is to:

-Practice loading and exploring a real-world dataset

-Perform data cleaning and transformation

-Create basic visualizations (trends, journals, keywords)

-Build a Streamlit app for interactive exploration

-Document the workflow and insights




📂 Repository Structure
Frameworks_Assignment/
│
├── notebooks/              # Jupyter notebooks for data exploration
│   └── exploration.ipynb
│
├── app.py                  # Streamlit application
├── requirements.txt        # Required Python libraries
├── .gitignore              # Files ignored by Git
└── README.md               # Project documentation




📥 Dataset

-⚠️ The dataset is not included in this repo (because it’s too large).

-Download the metadata.csv file from Kaggle:

-👉 CORD-19 Research Challenge

Place it in the root of this project, like this:

Frameworks_Assignment/
│
├── metadata.csv   ← place file here
├── app.py
└── notebooks/




Open notebooks/exploration.ipynb and run the cells to explore:
-Data dimensions & types

-Missing values

-Publication trends by year

-Top journals

-Frequent keywords







Features:

-Slider to filter publications by year

-Bar chart of publications over time

-Top publishing journals

-Word cloud of research titles

-Sample data preview




📊 Example Visualizations

-Publications over time (2019–2021)

-Most common journals

-Word cloud of paper titles

-(Generated plots will appear inside the Streamlit app)



📝 Reflection

-Handling the dataset required sampling since metadata.csv is ~1.5 GB.

-Learned how to clean and preprocess large datasets using pandas.

-Built basic but meaningful visualizations to highlight COVID-19 research trends.

-First experience deploying results into an interactive web app with Streamlit.



📌 Evaluation Criteria

✅ Complete implementation of assignment tasks

✅ Clean, well-commented code

✅ Clear visualizations

✅ Working Streamlit app

✅ Documentation (this README + notebooks)




🙌 Acknowledgments

-Dataset: CORD-19 Kaggle Challenge

-Tools: Python, pandas, matplotlib, seaborn, Streamlit
