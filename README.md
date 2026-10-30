# FarmAssist – Smart Farming Assistant

## Project Overview
FarmAssist is a multilingual, weather-based crop recommendation application designed to help farmers understand local weather conditions and explore potentially suitable crops.

It provides weather forecasts, preliminary crop suitability analysis and district-specific agricultural guidance.

## Features

- **Location Selection:** Select State, District and Mandal.
- **Weather Information:** View current temperature, previous-hour rainfall and expected daily rainfall.
- **7-Day Forecast:** View temperature, rainfall and rainfall probability.
- **Crop Recommendations:** Get preliminary crop suggestions based on soil, irrigation and weather conditions.
- **Alternative Crop Analysis:** Understand why some crops may be less suitable.
- **Multilingual Interface:** English, Telugu and Hindi.
- **District Crop Guidance:** Displays initial source-backed contingency guidance for Adilabad, including Maize and Jowar.

## Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- Open-Meteo Weather API
- India LGD-based location data API
- Pytest

## Project Structure

```text
FarmAssist/
│
├── app.py
├── weather.py
├── location_data.py
├── recommendations.py
├── crop_guidance.py
├── tests/
│   └── test_recommendations.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd FarmAssist
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## How It Works

1. Select the language.
2. Select the state, district and mandal.
3. Enter soil type and irrigation availability.
4. Retrieve weather information.
5. View the seven-day weather forecast.
6. Explore preliminary crop recommendations.
7. Check available district-specific agricultural guidance.

## Important Limitations

- Crop recommendations currently use preliminary rule-based logic, not a trained machine learning model.
- Crop suitability scores are estimates, not yield predictions.
- District-specific verified guidance is currently limited to two Adilabad contingency records from a 2011 ICAR-CRIDA plan.
- Weather location matching may return a nearby or district-level location if the exact mandal cannot be identified.
- Weather forecasts depend on external API availability.
- Farmers should confirm decisions with local agricultural officers or experts.

## Data Sources

- Open-Meteo Weather API: https://open-meteo.com/
- India LGD-based location data API: https://india-lgd-index-api.vercel.app/
- ICAR-CRIDA Crop Contingency Plans: https://www.icar-crida.res.in/Crop_Contingency_Plan.html

## Future Enhancements

- Expand verified crop guidance across Indian states and districts.
- Improve recommendations using agricultural research data.
- Add crop disease identification.
- Add regional agricultural advisories.
- Improve location matching accuracy.

## Disclaimer

FarmAssist is an educational prototype. Its suggestions should not replace professional agricultural advice.
