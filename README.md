# Sales Data Science: TAL, Target Account List
## Identifying Leads accounts with high potential to conversion for a sales cockpit

This repository contains the code and data for a project aimed at identifying high-potential accounts for sales targeting. The objective is to develop a model to help the sales team prioritize accounts based on their likelihood of conversion.

## Project Structure

The project is organized into the following directories and files:

- `data/`: Contains the raw data files used for the analysis.
- `data_processed/`: Contains the processed data files after cleaning and preprocessing according to concatenation type.
  - `email/`
  - `engagement/`
  - `intent/`
  - `intersection/`
- `src/`: Contains the source code for the project.
  - `EDA/`: Contains notebooks and scripts for exploratory data analysis (EDA).
    - `notebooks/`
      - `1-eda-all.ipynb`: EDA on all datasets.
      - `2-dataset-preparation.ipynb`: Dataset preparation and cleaning.
      - `3-eda-train.ipynb`: EDA on the training dataset.
      - `4-eda-target-accounts.ipynb`: EDA on target accounts.
    - `scripts/`: Python scripts for EDA tasks.
  - `modelling/`: Contains notebooks and scripts for modelling.
    - `notebooks/`
      - `1-modelling-intersection.ipynb`: Modelling based on intersected data.
      - `2-modelling-email.ipynb`: Modelling based on email data.
      - `3-modelling-intent.ipynb`: Modelling based on intent data.
      - `4-modelling-engagement.ipynb`: Modelling based on engagement data.
      - `top_20_feature_importances.png`: Top 20 feature importances from the random forest model.
    - `scripts/`: Python scripts for modelling tasks.
  - `utils.py`: Utility functions used throughout the project.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies required to run the project.

## Data Description

- **Account Base File**: List of all accounts with unique ID (`id_number`) and basic account/firmographic data.
- **Email Action File**: Denotes email clicks or replies and the date of the actions.
- **Intent File**: Includes categories of affiliate sites visited by the account and the date of the action.
- **Engagement File**: Includes campaign engagement and website visit data with the date the action occurred.
- **Third Party Readiness Score File**: Includes an account readiness score from a third-party data provider.
- **Met Target Date File**: List of accounts that met the target (participated in a trial) and the date the target was met.

## Methodology

1. **Exploratory Data Analysis (EDA)**:
   - Performed EDA on each individual dataset to understand the data distribution and identify any patterns.
   - Processed and cleaned the data, handling missing values and ensuring data quality.

2. **Feature Engineering**:
   - Created features from the email interaction data, leads data, and intent data.
   - Calculated metrics such as average distance between interactions, total length of interaction in days, weekly engagement rate, etc.

3. **Handling Missing Data**:
   - Imputed missing data using the average to avoid adding noise and ensure truthful representation of interest and engagement.

4. **Feature Selection**:
   - Used a random forest model to identify the most important features.
   - Selected the top features for the modelling process.

5. **Model Selection & Evaluation**:
   - Implemented additive logistic regression, iteratively adding the most important features and evaluating the model using AUC for train and validation data.
   - Compared the performance of the logistic regression model with the random forest model.

6. **Prediction & Insights**:
   - Made predictions on the test data using models with the top 4 and top 10 features.
   - Identified potential high-value accounts based on predicted probabilities and ranked them by their likelihood of conversion.
   - Assessed the potential revenue impact of targeting these accounts.

## Logistic Regression Equations

Logistic regression is a statistical method for predicting binary outcomes from data. The logistic regression model predicts the probability that a given instance belongs to a certain class.

The logistic regression model is defined as:

$$
P(y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_nX_n)}} 
$$

where:

- $P(y=1|X)$ is the probability of the instance being in class 1.
- $\beta_0$ is the intercept term.
- $\beta_1, \beta_2, ..., \beta_n$ are the coefficients for the predictor variables $X_1, X_2, ..., X_n$.

The log-odds or logit transformation is given by:

$$
 \ln\left(\frac{P}{1-P}\right) = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_nX_n 
 $$

To obtain the probability $P $ from the log-odds, we use the logistic function:

$$ P = \frac{1}{1 + e^{-\text{logit}(P)}} $$

### Meaning of the Probability

- The probability $P(y=1|X)$ represents the likelihood that the given instance belongs to class 1 (e.g., an account will convert).
- A higher probability indicates a higher likelihood of the account converting, allowing the sales team to prioritize these accounts.
- The logistic function ensures that the output is between 0 and 1, making it interpretable as a probability.

## Results

- Identified 30 potential companies with a high probability of conversion.
- Ranked these companies based on their size and conversion probability.
- Estimated a cumulative yearly revenue payoff from these accounts.

## How to Run

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Navigate to the `src/EDA/notebooks` and `src/modelling/notebooks` directories to explore the Jupyter notebooks for EDA and modelling.

## Conclusion

This project provides a comprehensive approach to identifying high-potential accounts for sales targeting using data-driven methods. The EDA, feature engineering, and modelling steps are well-documented in the notebooks, ensuring reproducibility and transparency.
