
import streamlit as st
import pandas as pd

from weather import get_coordinates, get_weather

from location_data import (
    get_state_names,
    get_district_names,
    get_subdistrict_names,
    get_source_date
)

from recommendations import get_crop_recommendations
from crop_guidance import get_district_guidance


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="FarmAssist",
    page_icon="🌱",
    layout="wide"
)


# --------------------------------------------------
# TRANSLATIONS
# --------------------------------------------------

TEXT = {
    "English": {
        "title": "FarmAssist - Smart Farming Assistant",
        "subtitle": "Weather-Based Smart Crop Recommendation System",
        "language": "Select Language",
        "location": "Farming Location",
        "state": "Select State / Union Territory",
        "district": "Select District",
        "mandal": "Select Mandal / Taluk",
        "farm": "Farm Details",
        "soil": "Select Soil Type",
        "irrigation": "Irrigation Availability",
        "button": "Get Weather & Crop Recommendations",
        "loading_location": "Loading location information...",
        "loading_weather": "Fetching weather information...",
        "current": "Current Weather",
        "temperature": "Current Temperature",
        "rain": "Rainfall (Previous Hour)",
        "today_rain": "Today's Expected Rainfall",
        "feels": "Feels Like",
        "forecast": "7-Day Weather Forecast",
        "date": "Date",
        "min": "Minimum Temperature (°C)",
        "max": "Maximum Temperature (°C)",
        "rainfall": "Rainfall (mm)",
        "probability": "Rain Probability (%)",
        "temperature_chart": "Temperature Forecast",
        "rain_chart": "Daily Rainfall Forecast",
        "crop_analysis": "Crop Suitability Analysis",
        "season": "Current Agricultural Season",
        "score_note": "Suitability scores are preliminary rule-based estimates, not guaranteed crop success or yield predictions.",
        "recommended": "Top Recommended Crops",
        "why": "Why is this crop suitable?",
        "water": "Water Management",
        "check": "Things to Check",
        "other": "Other Crops and Why They May Be Less Suitable",
        "less_note": "This is a preliminary screening result, not a recommendation to permanently avoid this crop.",
        "no_crop": "No crop passed the current screening rules. Consult your local agricultural officer.",
        "location_error": "Unable to load location information. Please try again.",
        "weather_error": "Unable to fetch weather information. Check your internet connection and location.",
        "location_match": "Weather location matched",
        "verify": "Mandal-level location could not be confirmed. Weather may represent a nearby or district-level location.",
        "disclaimer": "FarmAssist provides general weather-based and rule-based suggestions. Confirm sowing dates, soil suitability and seed varieties with your local agricultural expert.",
        "source": "Location data source",
        "soil_names": {
            "Red": "Red Soil",
            "Black": "Black Soil",
            "Sandy": "Sandy Soil",
            "Alluvial": "Alluvial Soil",
            "Unknown": "Don't Know"
        },
        "water_names": {
            "Available": "Available throughout the year",
            "Limited": "Limited water",
            "Rainfed": "Rainfed only"
        },
        "crops": {
            "Bengal Gram (Chickpea)": "Bengal Gram (Chickpea)",
            "Mustard": "Mustard",
            "Wheat": "Wheat",
            "Maize": "Maize",
            "Groundnut": "Groundnut",
            "Sorghum (Jowar)": "Sorghum (Jowar)",
            "Rice (Paddy)": "Rice (Paddy)",
            "Cotton": "Cotton",
            "Soybean": "Soybean",
            "Lentil": "Lentil"
        }
    },

    "Telugu": {
        "title": "ఫార్మ్ అసిస్ట్ - స్మార్ట్ వ్యవసాయ సహాయకుడు",
        "subtitle": "వాతావరణ ఆధారిత పంటల సిఫార్సు వ్యవస్థ",
        "language": "భాషను ఎంచుకోండి",
        "location": "వ్యవసాయ ప్రాంతం",
        "state": "రాష్ట్రం / కేంద్రపాలిత ప్రాంతాన్ని ఎంచుకోండి",
        "district": "జిల్లాను ఎంచుకోండి",
        "mandal": "మండలం / తాలూకాను ఎంచుకోండి",
        "farm": "వ్యవసాయ భూమి వివరాలు",
        "soil": "నేల రకాన్ని ఎంచుకోండి",
        "irrigation": "నీటి సదుపాయం",
        "button": "వాతావరణం మరియు పంటల సూచనలు పొందండి",
        "loading_location": "ప్రాంత వివరాలను పొందుతున్నాము...",
        "loading_weather": "వాతావరణ వివరాలను పొందుతున్నాము...",
        "current": "ప్రస్తుత వాతావరణం",
        "temperature": "ప్రస్తుత ఉష్ణోగ్రత",
        "rain": "గత ఒక గంటలో వర్షపాతం",
        "today_rain": "ఈరోజు అంచనా వర్షపాతం",
        "feels": "అనుభూతి ఉష్ణోగ్రత",
        "forecast": "7 రోజుల వాతావరణ అంచనా",
        "date": "తేదీ",
        "min": "కనిష్ట ఉష్ణోగ్రత (°C)",
        "max": "గరిష్ట ఉష్ణోగ్రత (°C)",
        "rainfall": "వర్షపాతం (mm)",
        "probability": "వర్షం పడే అవకాశం (%)",
        "temperature_chart": "ఉష్ణోగ్రత అంచనా",
        "rain_chart": "రోజువారీ వర్షపాతం అంచనా",
        "crop_analysis": "పంటల అనుకూలత విశ్లేషణ",
        "season": "ప్రస్తుత వ్యవసాయ సీజన్",
        "score_note": "ఈ అనుకూలత స్కోర్లు ప్రాథమిక నియమాల ఆధారంగా రూపొందించబడ్డాయి. ఇవి పంట దిగుబడికి హామీ కావు.",
        "recommended": "అత్యంత అనుకూలమైన పంటలు",
        "why": "ఈ పంట ఎందుకు అనుకూలం?",
        "water": "నీటి నిర్వహణ",
        "check": "గమనించాల్సిన విషయాలు",
        "other": "ఇతర పంటలు ఎందుకు తక్కువ అనుకూలం?",
        "less_note": "ఇది ప్రాథమిక అంచనా మాత్రమే. ఈ పంటను పూర్తిగా సాగు చేయకూడదని అర్థం కాదు.",
        "no_crop": "ప్రస్తుత నియమాల ప్రకారం ఏ పంటా అనుకూలత ప్రమాణాలను చేరుకోలేదు. స్థానిక వ్యవసాయ అధికారిని సంప్రదించండి.",
        "location_error": "ప్రాంత వివరాలను పొందలేకపోయాము. మళ్లీ ప్రయత్నించండి.",
        "weather_error": "వాతావరణ వివరాలను పొందలేకపోయాము. ఇంటర్నెట్ మరియు ప్రాంత వివరాలను తనిఖీ చేయండి.",
        "location_match": "వాతావరణం కోసం గుర్తించిన ప్రాంతం",
        "verify": "మండలం ఖచ్చితంగా గుర్తించబడలేదు. వాతావరణ వివరాలు సమీప ప్రాంతం లేదా జిల్లా స్థాయికి సంబంధించినవి కావచ్చు.",
        "disclaimer": "ఫార్మ్ అసిస్ట్ సాధారణ వాతావరణ మరియు నియమాల ఆధారిత సూచనలు అందిస్తుంది. విత్తే సమయం, నేల అనుకూలత మరియు విత్తన రకాలను స్థానిక వ్యవసాయ నిపుణులతో నిర్ధారించుకోండి.",
        "source": "ప్రాంత వివరాల మూలం",
        "soil_names": {
            "Red": "ఎర్ర నేల",
            "Black": "నల్ల నేల",
            "Sandy": "ఇసుక నేల",
            "Alluvial": "ఒండ్రు నేల",
            "Unknown": "తెలియదు"
        },
        "water_names": {
            "Available": "ఏడాది పొడవునా నీరు అందుబాటులో ఉంది",
            "Limited": "పరిమిత నీటి సదుపాయం",
            "Rainfed": "వర్షాధార సాగు మాత్రమే"
        },
        "crops": {
            "Bengal Gram (Chickpea)": "శనగలు",
            "Mustard": "ఆవాలు",
            "Wheat": "గోధుమలు",
            "Maize": "మొక్కజొన్న",
            "Groundnut": "వేరుశనగ",
            "Sorghum (Jowar)": "జొన్నలు",
            "Rice (Paddy)": "వరి",
            "Cotton": "పత్తి",
            "Soybean": "సోయాబీన్",
            "Lentil": "మసూర్ పప్పు"
        }
    },

    "Hindi": {
        "title": "फार्म असिस्ट - स्मार्ट कृषि सहायक",
        "subtitle": "मौसम आधारित फसल सुझाव प्रणाली",
        "language": "भाषा चुनें",
        "location": "खेती का स्थान",
        "state": "राज्य / केंद्र शासित प्रदेश चुनें",
        "district": "जिला चुनें",
        "mandal": "मंडल / तालुका चुनें",
        "farm": "खेत की जानकारी",
        "soil": "मिट्टी का प्रकार चुनें",
        "irrigation": "सिंचाई की सुविधा",
        "button": "मौसम और फसल सुझाव प्राप्त करें",
        "loading_location": "स्थान की जानकारी प्राप्त की जा रही है...",
        "loading_weather": "मौसम की जानकारी प्राप्त की जा रही है...",
        "current": "वर्तमान मौसम",
        "temperature": "वर्तमान तापमान",
        "rain": "पिछले एक घंटे की वर्षा",
        "today_rain": "आज की अनुमानित वर्षा",
        "feels": "महसूस होने वाला तापमान",
        "forecast": "7 दिनों का मौसम पूर्वानुमान",
        "date": "तारीख",
        "min": "न्यूनतम तापमान (°C)",
        "max": "अधिकतम तापमान (°C)",
        "rainfall": "वर्षा (mm)",
        "probability": "बारिश की संभावना (%)",
        "temperature_chart": "तापमान पूर्वानुमान",
        "rain_chart": "दैनिक वर्षा पूर्वानुमान",
        "crop_analysis": "फसल उपयुक्तता विश्लेषण",
        "season": "वर्तमान कृषि मौसम",
        "score_note": "ये उपयुक्तता स्कोर प्रारंभिक नियमों पर आधारित हैं। ये फसल की सफलता या उपज की गारंटी नहीं हैं।",
        "recommended": "सबसे उपयुक्त फसलें",
        "why": "यह फसल क्यों उपयुक्त है?",
        "water": "जल प्रबंधन",
        "check": "ध्यान देने योग्य बातें",
        "other": "अन्य फसलें कम उपयुक्त क्यों हैं?",
        "less_note": "यह एक प्रारंभिक जाँच है। इसका अर्थ यह नहीं है कि इस फसल को कभी नहीं उगाना चाहिए।",
        "no_crop": "वर्तमान नियमों के अनुसार कोई फसल उपयुक्तता मानदंडों पर खरी नहीं उतरी। स्थानीय कृषि अधिकारी से सलाह लें।",
        "location_error": "स्थान की जानकारी प्राप्त नहीं हो सकी। कृपया पुनः प्रयास करें।",
        "weather_error": "मौसम की जानकारी प्राप्त नहीं हो सकी। इंटरनेट और स्थान विवरण जाँचें।",
        "location_match": "मौसम के लिए पहचाना गया स्थान",
        "verify": "मंडल की पुष्टि नहीं हो सकी। पूर्वानुमान पास के क्षेत्र या जिले का हो सकता है।",
        "disclaimer": "फार्म असिस्ट सामान्य मौसम और नियम आधारित सुझाव देता है। बुवाई का समय, मिट्टी और बीज की किस्म स्थानीय कृषि विशेषज्ञ से सुनिश्चित करें।",
        "source": "स्थान डेटा स्रोत",
        "soil_names": {
            "Red": "लाल मिट्टी",
            "Black": "काली मिट्टी",
            "Sandy": "रेतीली मिट्टी",
            "Alluvial": "जलोढ़ मिट्टी",
            "Unknown": "पता नहीं"
        },
        "water_names": {
            "Available": "पूरे वर्ष पानी उपलब्ध",
            "Limited": "सीमित पानी",
            "Rainfed": "केवल वर्षा आधारित"
        },
        "crops": {
            "Bengal Gram (Chickpea)": "चना",
            "Mustard": "सरसों",
            "Wheat": "गेहूँ",
            "Maize": "मक्का",
            "Groundnut": "मूंगफली",
            "Sorghum (Jowar)": "ज्वार",
            "Rice (Paddy)": "धान",
            "Cotton": "कपास",
            "Soybean": "सोयाबीन",
            "Lentil": "मसूर"
        }
    }
}


# --------------------------------------------------
# LANGUAGE SELECTION
# --------------------------------------------------

language = st.selectbox(
    "Language / భాష / भाषा",
    ["English", "Telugu", "Hindi"]
)

t = TEXT[language]

st.title("🌱 " + t["title"])
st.write(t["subtitle"])


# --------------------------------------------------
# LOCATION SELECTION
# --------------------------------------------------

st.header("📍 " + t["location"])

try:
    with st.spinner(t["loading_location"]):

        states = get_state_names()

        if not states:
            st.error(t["location_error"])
            st.stop()

        state_names = [item["name"] for item in states]

        default_index = next(
            (
                i for i, name in enumerate(state_names)
                if name.lower() == "telangana"
            ),
            0
        )

        selected_state = st.selectbox(
            t["state"],
            states,
            index=default_index,
            format_func=lambda item: item["name"]
        )

        districts = get_district_names(
            str(selected_state["code"])
        )

        if not districts:
            st.warning(t["location_error"])
            st.stop()

        selected_district = st.selectbox(
            t["district"],
            districts,
            format_func=lambda item: item["name"]
        )

        subdistricts = get_subdistrict_names(
            str(selected_district["code"])
        )

        if not subdistricts:
            st.warning(t["location_error"])
            st.stop()

        selected_mandal = st.selectbox(
            t["mandal"],
            subdistricts,
            format_func=lambda item: item["name"]
        )

    state = selected_state["name"]
    district = selected_district["name"]
    mandal = selected_mandal["name"]

    st.caption(
        f"{t['source']}: LGD | Data edition: {get_source_date()}"
    )

except Exception as error:
    st.error(t["location_error"])
    st.caption(f"Technical details: {error}")
    st.stop()


# --------------------------------------------------
# FARM DETAILS
# --------------------------------------------------

st.header("🌾 " + t["farm"])

soil_options = ["Red", "Black", "Sandy", "Alluvial", "Unknown"]

soil = st.selectbox(
    t["soil"],
    soil_options,
    format_func=lambda value: t["soil_names"][value]
)

irrigation_options = ["Available", "Limited", "Rainfed"]

irrigation = st.selectbox(
    t["irrigation"],
    irrigation_options,
    format_func=lambda value: t["water_names"][value]
)


# --------------------------------------------------
# WEATHER AND CROP ANALYSIS
# --------------------------------------------------

if st.button(t["button"], type="primary"):

    try:
        with st.spinner(t["loading_weather"]):

            location = get_coordinates(
                state,
                district,
                mandal
            )

            weather = get_weather(
                location["latitude"],
                location["longitude"]
            )

        # Verify whether geocoder found the requested mandal.
        matched_query = location.get("matched_query", "")

        st.success(
            f"{t['location_match']}: {location['name']}"
        )

        if not matched_query.startswith(f"{mandal},"):
            st.warning(t["verify"])

        current = weather["current"]
        daily = weather["daily"]

        temperature = current["temperature_2m"]
        previous_hour_rainfall = current.get("precipitation", 0.0)
        today_expected_rainfall = daily["precipitation_sum"][0]

        # --------------------------------------------------
        # CURRENT WEATHER
        # --------------------------------------------------

        st.header("🌤️ " + t["current"])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                t["temperature"],
                f"{temperature} °C"
            )

        with col2:
            st.metric(
                t["rain"],
                f"{previous_hour_rainfall} mm"
            )

        with col3:
            st.metric(
                t["today_rain"],
                f"{today_expected_rainfall} mm"
            )

        apparent = current.get("apparent_temperature")

        if apparent is not None:
            st.caption(
                f"{t['feels']}: {apparent} °C"
            )

        # --------------------------------------------------
        # 7-DAY WEATHER FORECAST
        # --------------------------------------------------

        st.header("📅 " + t["forecast"])

        forecast_df = pd.DataFrame({
            t["date"]: daily["time"],
            t["min"]: daily["temperature_2m_min"],
            t["max"]: daily["temperature_2m_max"],
            t["rainfall"]: daily["precipitation_sum"],
            t["probability"]: daily["precipitation_probability_max"]
        })

        st.dataframe(
            forecast_df,
            use_container_width=True,
            hide_index=True
        )

        st.subheader(t["temperature_chart"])

        temperature_chart = forecast_df.set_index(t["date"])[
            [t["min"], t["max"]]
        ]

        st.line_chart(temperature_chart)

        st.subheader(t["rain_chart"])

        rainfall_chart = forecast_df.set_index(t["date"])[
            t["rainfall"]
        ]

        st.bar_chart(rainfall_chart)

        # --------------------------------------------------
        # CROP SUITABILITY ANALYSIS
        # --------------------------------------------------

        st.header("🌱 " + t["crop_analysis"])

        forecast_rainfall = daily["precipitation_sum"][0] or 0

        rainfall_probability = (
            daily["precipitation_probability_max"][0] or 0
        )

        analysis = get_crop_recommendations(
            soil=soil,
            irrigation=irrigation,
            temperature=temperature,
            rainfall_mm=forecast_rainfall,
            rainfall_probability=rainfall_probability,
            language=language
        )

        st.info(
            f"{t['season']}: {analysis['season']}"
        )

        st.caption(t["score_note"])

        # --------------------------------------------------
        # TOP RECOMMENDED CROPS
        # --------------------------------------------------

        st.subheader("✅ " + t["recommended"])

        if analysis["recommended"]:

            for index, crop in enumerate(
                analysis["recommended"],
                start=1
            ):

                crop_name = t["crops"].get(
                    crop["crop"],
                    crop["crop"]
                )

                with st.expander(
                    f"{index}. {crop_name} - {crop['score']}%",
                    expanded=True
                ):

                    st.write(crop["general_reason"])

                    st.write("**" + t["why"] + "**")

                    for reason in crop["reasons"]:
                        st.write("✓ " + reason)

                    st.write("**" + t["water"] + ":**")

                    st.write(crop["water_note"])

                    if crop["concerns"]:

                        st.write("**" + t["check"] + ":**")

                        for concern in crop["concerns"]:
                            st.write("⚠️ " + concern)

        else:
            st.warning(t["no_crop"])

        # --------------------------------------------------
        # OTHER / LESS SUITABLE CROPS
        # --------------------------------------------------

        st.subheader("⚠️ " + t["other"])

        for crop in analysis["less_suitable"]:

            crop_name = t["crops"].get(
                crop["crop"],
                crop["crop"]
            )

            with st.expander(crop_name):

                if crop["concerns"]:

                    for concern in crop["concerns"]:
                        st.write("• " + concern)

                st.caption(t["less_note"])

        # --------------------------------------------------
        # VERIFIED DISTRICT CROP GUIDANCE
        # --------------------------------------------------

        guidance_text = {
            "English": {
                "title": "Verified District Crop Guidance",
                "condition": "Applicable condition",
                "reason": "Why this crop is suggested",
                "soil": "Soil",
                "water": "Water requirement",
                "source": "Source",
                "view_plan": "View Original Agricultural Plan",
                "warning": (
                    "This is historical contingency guidance from 2011. "
                    "It is not a current-season guarantee. Confirm with "
                    "your local agricultural officer."
                ),
                "empty": (
                    "No verified district-specific records are available "
                    "for this location yet."
                )
            },
            "Telugu": {
                "title": "జిల్లా ఆధారిత ధృవీకరించిన పంటల సూచనలు",
                "condition": "వర్తించే పరిస్థితి",
                "reason": "ఈ పంటను ఎందుకు సూచించారు?",
                "soil": "నేల",
                "water": "నీటి అవసరం",
                "source": "మూలం",
                "view_plan": "వ్యవసాయ ప్రణాళికను చూడండి",
                "warning": (
                    "ఇది 2011 నాటి పాత వ్యవసాయ అత్యవసర సూచన. "
                    "ప్రస్తుత సీజన్‌కు హామీ కాదు. స్థానిక వ్యవసాయ "
                    "అధికారిని సంప్రదించండి."
                ),
                "empty": (
                    "ఈ ప్రాంతానికి ధృవీకరించిన జిల్లా స్థాయి "
                    "పంట వివరాలు ఇంకా అందుబాటులో లేవు."
                )
            },
            "Hindi": {
                "title": "सत्यापित जिला-आधारित फसल सुझाव",
                "condition": "लागू होने वाली स्थिति",
                "reason": "इस फसल का सुझाव क्यों दिया गया?",
                "soil": "मिट्टी",
                "water": "पानी की आवश्यकता",
                "source": "स्रोत",
                "view_plan": "मूल कृषि योजना देखें",
                "warning": (
                    "यह 2011 की पुरानी आकस्मिक कृषि सलाह है। "
                    "यह वर्तमान मौसम की गारंटी नहीं है। "
                    "स्थानीय कृषि अधिकारी से सलाह लें।"
                ),
                "empty": (
                    "इस स्थान के लिए सत्यापित जिला-स्तरीय "
                    "फसल रिकॉर्ड अभी उपलब्ध नहीं हैं।"
                )
            }
        }

        gt = guidance_text[language]

        st.header("📚 " + gt["title"])

        district_guidance = get_district_guidance(
            state=state,
            district=district
        )

        if district_guidance:
            for record in district_guidance:
                st.subheader("🌾 " + record["crop"])

                st.write(
                    f"**{gt['condition']}:** {record['condition']}"
                )
                st.write(
                    f"**{gt['reason']}:** {record['reason']}"
                )
                st.write(
                    f"**{gt['soil']}:** {', '.join(record['soil'])}"
                )
                st.write(
                    f"**{gt['water']}:** {record['water']}"
                )
                st.caption(
                    f"{gt['source']}: {record['source_name']} "
                    f"({record['source_year']})"
                )
                st.link_button(
                    gt["view_plan"],
                    record["source_url"]
                )

            st.warning(gt["warning"])
        else:
            st.info(gt["empty"])

        # --------------------------------------------------
        # DISCLAIMER
        # --------------------------------------------------

        st.divider()

        st.caption(t["disclaimer"])

    except Exception as error:

        st.error(t["weather_error"])

        st.caption(
            f"Technical details: {error}"
        )
